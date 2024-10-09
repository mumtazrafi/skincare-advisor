from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "your-username/llama-skincare-advisor"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

skincare_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

def get_skincare_recommendation(skin_type, concern):
    prompt = f"Skin Type: {skin_type}\nConcern: {concern}\nRecommendation:"
    response = skincare_pipeline(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    return response.split("Recommendation:")[1].strip()

# Example usage
skin_type = "Oily"
concern = "Acne"
recommendation = get_skincare_recommendation(skin_type, concern)
print(f"Recommendation for {skin_type} skin with {concern} concern:")
print(recommendation)