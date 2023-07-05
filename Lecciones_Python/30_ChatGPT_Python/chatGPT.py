import openai
from rich import print

openai.api_key = "tu_clave_de_api"

print("[bold red]ChatGPT en Python[/bold red]") 
contexto = {"role": "system", "content": "Sabes todo lo que te pregunto"}
messages = [contexto]

while True:
    content = input("\nDime de qué quieres hablar, breativo: ")  

    if content == "exit":
        break
    
    messages.append({"role": "user", "content": content})
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=messages,
        max_tokens=50
    )
    
    response_messages = response.choices[0].text.strip()
    
    messages.append({"role": "assistant", "content": response_messages})
    print(response_messages)
