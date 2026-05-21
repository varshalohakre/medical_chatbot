# medical_chatbot

# how to create build the project

# how to run
### STEPS: 

clone the repository
```bash
git clone https://github.com/varshalohakre/medical_chatbot.git
```

### STEP 01 - create anaconda environment after opening repository

```bash
conda create -n medibot python-3.10 -y
```

```bash
conda activate medibot
```

### STEP2 
```bash
pip install requirements.txt
```


A production-ready AI-powered Medical Chatbot that answers disease-related queries using Retrieval-Augmented Generation (RAG) with LangChain, Pinecone vector database, and a Large Language Model — deployed on AWS with CI/CD via GitHub Actions.

📁 Project Structure
medical_chatbot/
├── src/
│   └── helper.py          # PDF loader, embeddings, text splitter
├── templates/
│   └── chat.html          # Frontend chat interface
├── data/                  # Medical PDF knowledge base
├── app.py                 # Flask application
├── store_index.py         # Embed & upsert data to Pinecone
├── requirements.txt
├── .env                   # API keys (never commit this)
├── Dockerfile
└── README.md

🚀 How to Run Locally
Step 1 — Clone the Repository
bashgit clone  https://github.com/varshalohakre/medical_chatbot.git
cd medical_chatbot
Step 2 — Create & Activate Conda Environment
bashconda create -n medibot python=3.10 -y
conda activate medibot
Step 3 — Install Dependencies
bashpip install -r requirements.txt
Step 4 — Configure Environment Variables
Create a .env file in the root directory of the project:
iniPINECONE_API_KEY=your_pinecone_api_key_here
GROQ_API_KEY=your_groq_api_key_here

⚠️ Never commit your .env file. Make sure it is listed in .gitignore.

Step 5 — Store Embeddings in Pinecone
Run this once to load PDFs, generate embeddings, and upsert them into your Pinecone index:
bashpython store_index.py
Step 6 — Run the Application
bashpython app.py
Then open your browser and navigate to:
http://localhost:5000

🛠️ Tech Stack
LayerTechnologyLanguagePython 3.10FrameworkFlaskLLMOpenAI GPTEmbeddingsHuggingFace / OpenAIVector StorePineconeOrchestrationLangChainFrontendHTML, CSS, JavaScriptDeploymentAWS EC2 + ECRCI/CDGitHub ActionsContainerizationDocker

☁️ AWS CI/CD Deployment with GitHub Actions
1. Login to AWS Console
Go to https://aws.amazon.com and sign in.

2. Create an IAM User for Deployment
Create an IAM user with programmatic access and attach the following policies:
✅ AmazonEC2ContainerRegistryFullAccess
✅ AmazonEC2FullAccess

This user will be used by GitHub Actions to push Docker images to ECR and deploy to EC2.


3. Create an ECR Repository
Create a private ECR repository to store your Docker image.
Save the repository URI — you will need it as a GitHub secret:
315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot

4. Create an EC2 Instance (Ubuntu)
Launch an EC2 instance with Ubuntu. Make sure port 5000 (or your app port) is open in the security group inbound rules.

5. Install Docker on the EC2 Instance
SSH into your EC2 instance and run:
bash# Update packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add ubuntu user to docker group
sudo usermod -aG docker ubuntu
newgrp docker

6. Configure EC2 as a GitHub Self-Hosted Runner
In your GitHub repository:
Settings → Actions → Runners → New self-hosted runner
Choose Linux as the OS and follow the commands shown on screen — run them one by one on your EC2 instance.

7. Add GitHub Actions Secrets
In your GitHub repository go to:
Settings → Secrets and variables → Actions → New repository secret
Add the following secrets:
Secret NameDescriptionAWS_ACCESS_KEY_IDIAM user access keyAWS_SECRET_ACCESS_KEYIAM user secret keyAWS_DEFAULT_REGIONe.g. us-east-1ECR_REPOFull ECR URI e.g. 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbotPINECONE_API_KEYYour Pinecone API keyOPENAI_API_KEYYour OpenAI API key

Deployment Flow Summary
Code Push → GitHub Actions Trigger
        → Build Docker Image
        → Push Image to AWS ECR
        → SSH into EC2 via Self-Hosted Runner
        → Pull Image from ECR
        → Run Docker Container on EC2

📌 Notes

Run store_index.py only once (or when your knowledge base changes). It takes time to embed all PDFs.
Make sure your Pinecone index name in store_index.py and app.py match exactly.
The .env file must be in the project root, not inside src/.

