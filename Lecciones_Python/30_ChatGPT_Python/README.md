# ChatGPT Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 30. ChatGPT Python.

<h2 style="color:#15A7E1">ChatGPT.</h2>
Para conectar ChatGPT con Python, puedes utilizar la biblioteca 'openai' de OpenAI. 

<h2 style="color:#15A7E1">openai.</h2>

La biblioteca openai en Python es una herramienta proporcionada por OpenAI para interactuar con sus servicios de inteligencia artificial, como la API de GPT-3. Esta biblioteca facilita la comunicación con los modelos de lenguaje de OpenAI y simplifica la generación de texto a través de su API.

La biblioteca openai proporciona métodos y funciones que permiten enviar solicitudes a la API de OpenAI para generar texto. Aquí hay una descripción general de las principales características y componentes de la biblioteca:

* Configuración de la clave de API: Antes de utilizar la biblioteca, debes configurar tu clave de API proporcionada por OpenAI. Esto se realiza estableciendo la variable openai.api_key con tu clave de API.

* Funciones de generación de texto: La biblioteca openai incluye funciones para generar texto utilizando modelos de lenguaje pre-entrenados. La función principal para generar texto es openai.Completion.create(). Puedes proporcionar un prompt (texto inicial) y otros parámetros para obtener respuestas generadas por el modelo.

* Parámetros de generación: Al llamar a la función openai.Completion.create(), puedes especificar varios parámetros para controlar el comportamiento del modelo de generación de texto. Algunos parámetros comunes incluyen engine (motor de modelo a utilizar), temperature (que controla la aleatoriedad de las respuestas) y max_tokens (la longitud máxima del texto generado).

* Objetos de respuesta: Cuando se realiza una solicitud a la API de OpenAI, se devuelve un objeto de respuesta que contiene la salida generada por el modelo. Puedes acceder a diferentes atributos de este objeto de respuesta, como response.choices[0].text, que contiene el texto generado.

<h2 style="color:#15A7E1">Conectar ChatGPT.</h2>
Lo primero que debemos obtener es una clave de API de OpenAI, esta clave se obtiene en la web  de OpenAI, registrando tu cuneta para obtener la API valida.

Una vez instalada la biblioteca openai y disponemos de la clave. El siguiente paso es realizar una llamada a la función `open.Completion.create()` y acceder a la respuesta  generada por el modelo indicado a traves del atributo `response.choices[0].text`

Estos son solo los pasos básicos para establecer una conexión con ChatGPT utilizando Python. Puedes ajustar los parámetros y opciones según tus necesidades. Recuerda que ChatGPT es un modelo generativo y, por lo tanto, es posible que debas realizar un filtrado adicional o ajustes en la salida generada para obtener resultados óptimos.

<br>
<br>

````py
# Entrada
import openai
from rich import print

openai.api_key = "tu_clave_de_api"

print("[bold red]ChatGPT en Python[/bold red]") 
contexto = {"role": "system", "content": "Sabes todo lo que te pregunto"}
messages = [contexto]

while True:
    content = input("\nDime de qué quieres hablar, creativo: ")  

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

````

<br>
<br>

🎉 Enhorabuena has superado el curso. Lo que significa que has alcanzado los conocimientos básicos en Python. 🎉

<br>

[<< 29 Bases datos MYSQL](../29_MYSQL_Python) 

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)


