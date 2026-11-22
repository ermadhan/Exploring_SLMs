from litellm import completion

print('Sending request to Ollama LLaMA3 model...')

response = completion(
    model="ollama_chat/llama3.1:latest",
    messages=[{
        "content": "Briefly answer the following question, please. What would be the best movie to show an alien?",
        "role": "user"
    }],
    api_base="http://localhost:11434"
)

print(response.choices[0]["message"].content)