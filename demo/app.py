import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "skincare-reccomendationr"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

skincare_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

def skincare_advisor(skin_type, concern):
    prompt = f"Skin Type: {skin_type}\nConcern: {concern}\nRecommendation:"
    response = skincare_pipeline(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    return response.split("Recommendation:")[1].strip()

iface = gr.Interface(
    fn=skincare_advisor,
    inputs=[
        gr.Dropdown(["Oily", "Dry", "Combination", "Sensitive", "Normal"], label="Skin