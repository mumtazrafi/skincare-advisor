import pandas as pd
import random

# Define lists for each category
skin_types = ['Oily', 'Dry', 'Combination', 'Sensitive', 'Normal']
concerns = ['Acne', 'Wrinkles', 'Dullness', 'Redness', 'Uneven Texture', 'Hyperpigmentation']
product_types = ['Cleanser', 'Moisturizer', 'Serum', 'Sunscreen', 'Toner', 'Exfoliant']
ingredients = ['Salicylic Acid', 'Retinol', 'Vitamin C', 'Niacinamide', 'Hyaluronic Acid', 'Glycolic Acid']

def generate_recommendation(skin_type, concern, product_type, ingredient):
    return f"For {skin_type.lower()} skin with {concern.lower()} concerns, use a {product_type.lower()} containing {ingredient} to address the issue effectively."

# Generate 1000 entries
data = []
for _ in range(1000):
    skin_type = random.choice(skin_types)
    concern = random.choice(concerns)
    product_type = random.choice(product_types)
    ingredient = random.choice(ingredients)
    recommendation = generate_recommendation(skin_type, concern, product_type, ingredient)
    data.append({
        'Skin Type': skin_type,
        'Concern': concern,
        'Product Type': product_type,
        'Ingredient': ingredient,
        'Recommendation': recommendation
    })

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('../data/large_skincare_dataset.csv', index=False)
print("Dataset generated and saved successfully!")