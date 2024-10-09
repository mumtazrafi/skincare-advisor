# Skincare Advisor AI

## Overview
Skincare Advisor AI is a machine learning model based on Llama 3.2 1B, fine-tuned to provide personalized skincare recommendations. It takes into account a user's skin type and concerns to suggest appropriate skincare products and ingredients.

## Features
- Personalized skincare recommendations
- Support for various skin types and concerns
- Integration with Hugging Face for easy deployment

## Installation
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Follow the setup guide in `docs/setup_guide.md`

## Usage
```python
from inference import get_skincare_recommendation

skin_type = "Oily"
concern = "Acne"
recommendation = get_skincare_recommendation(skin_type, concern)
print(recommendation)
```

## Model
The model is hosted on Hugging Face: [your-username/llama-skincare-advisor](https://huggingface.co/your-username/llama-skincare-advisor)

## Demo
Try out the live demo: [Skincare Advisor AI Demo](https://huggingface.co/spaces/your-username/skincare-advisor-demo)

## Contributing
We welcome contributions! Please see our contributing guidelines for more details.

## License
This project is licensed under the MIT License - see the LICENSE file for details.