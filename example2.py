from litellm import completion

print('Sending request to Ollama LLaMA3 model...')

def get_director(movie):
    # first we create the prompt
    prompt = """
Please write a Wikidata query to find who is the director  of "{movie}".
Return only the query, not explanation.
    """.format(movie=movie).strip()

    print("Prompt:")
    print(prompt)
    print()

    # we will use the same call from above. The temperature is set to 0.1,
    # If you want to experiment with trying to get better results, perhaps
    # add a function argument for temperature.
    response = completion(
        model="ollama_chat/llama3.1",
        messages=[{
            "content": prompt,
            "role": "user"
        }],
        temperature=0.1,
        api_base="http://localhost:11434"
    )

    # This query often return markdown ticks, so we remove that.
    print("Query:")
    query = response.choices[0]["message"].content.strip("`").strip()
    print(query)
    return query

print(get_director("John Carter"))