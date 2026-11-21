# Exploring_SLMs
Project to explore difference SLMs for learning purpose

# Installation
-Install Miniconda - https://repo.anaconda.com/miniconda/

    In Windows machine, 
        • Open the Windows Start Menu, search for Anaconda Prompt, and open it.
        • Run conda init --all inside that window instead.

-Create envrionment for trying examples
    `conda create --name slmbook python=3.12`

-Activate the environment
    `conda activate slmbook`

-Install the required Python Data Packages captured in requirments.txt
    `pip install -r requirements.txt`

-Install the MCP framework.
    `conda install mcp`

-Install LiteLLM via PIP
    `pip install litellm`

-Install MongoDB

-Clone and Configure Librechat
    -Clone
        Go to D: drive
        mkdir D:\AI
        cd D:\AI
        git clone https://github.com/danny-avila/LibreChat.git
        cd D:\AI\LibreChat

        copy .env.example .env
        copy librechat.example.yaml librechat.yaml

    -Open D:\AI\LibreChat\librechat.yaml (notepad librechat.yaml) and add your Ollama endpoint under endpoints:
        `endpoints:`
            `custom:`
                `- name: "Ollama"`
                `apiKey: "ollama"`
                `baseURL: "http://localhost:11434/v1"`
                `models:`
                `default: ["llama3.2"]`
                `fetch: true`
                `titleConvo: true`
                `titleModel: "current_model"`

    -Install dependencies and build inside D:\AI\LibreChat and run front end and backend
        npm ci
        npm run frontend

        npm run backend

-Install Ollama and download model

-Acquiring the Data
    Wikipedia via MCP Server
    Wikidata using SPARQL Query

-Install Hugging Face Libraries into Conda
    `conda install -c huggingface -c conda-forge datasets huggingface_hub[cli]`

-Run the Jupyter server
    jupyter lab --no-browser


