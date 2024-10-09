from huggingface_hub import HfApi, Repository
import os

def upload_to_huggingface(local_dir, repo_name):
    api = HfApi()
    repo_url = api.create_repo(repo_name, exist_ok=True)
    
    repo = Repository(local_dir, clone_from=repo_url)
    
    for root, _, files in os.walk(local_dir):
        for file in files:
            file_path = os.path.join(root, file)
            repo.push_to_hub(commit_message=f"Upload {file}")
    
    print(f"All files uploaded to https://huggingface.co/{repo_name}")

# Usage
upload_to_huggingface("../", "your-username/llama-skincare-advisor")