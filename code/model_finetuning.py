import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# Load the model and tokenizer
model_name = "meta-llama/Llama-3.2-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Prepare the model for k-bit training
model = prepare_model_for_kbit_training(model)

# Define LoRA Config
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# Get the PEFT model
model = get_peft_model(model, lora_config)

# Load and preprocess your dataset
dataset = load_dataset("csv", data_files="../data/large_skincare_dataset.csv")

def preprocess_function(examples):
    inputs = [f"Skin Type: {skin_type}\nConcern: {concern}\nProduct Type: {product_type}\nIngredient: {ingredient}\n"
              for skin_type, concern, product_type, ingredient in zip(examples['Skin Type'], examples['Concern'], 
                                                                      examples['Product Type'], examples['Ingredient'])]
    targets = examples['Recommendation']
    
    model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
    labels = tokenizer(targets, max_length=128, truncation=True, padding="max_length")
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    fp16=True,
    save_total_limit=3,
    logging_steps=100,
    push_to_hub=True,
    hub_model_id="your-username/llama-skincare-advisor",
)

# Create Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    tokenizer=tokenizer,
)

# Train the model
trainer.train()

# Push the model to the Hub
trainer.push_to_hub()

print("Model fine-tuned and uploaded to Hugging Face successfully!")