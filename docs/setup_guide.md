# Skincare Advisor AI Setup Guide

## Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

## Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/your-username/skincare-advisor-ai.git
   cd skincare-advisor-ai
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up Hugging Face credentials:
   - Create an account on [Hugging Face](https://huggingface.co/)
   - Generate an access token in your account settings
   - Set the token as an environment variable:
     ```
     export HUGGINGFACE_TOKEN=your_token_here
     ```

5. Generate the dataset:
   ```
   python code/data_generation.py
   ```

6. Fine-tune the model:
   ```
   python code/model_finetuning.py
   ```

7. Run the inference script to test the model:
   ```
   python code/inference.py
   ```

## Troubleshooting
- If you encounter CUDA errors, ensure you have the correct version of PyTorch installed for your CUDA version.
- For any other issues, please check our FAQ or open an issue on GitHub.

## Next Steps
- Explore the `reports/` directory for data analysis and model performance insights.
- Check out the demo application in the `demo/` directory.
- Contribute to the project by following our contributing guidelines.