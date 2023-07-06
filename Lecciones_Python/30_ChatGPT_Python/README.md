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
import openai  # pip install openai
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table

def main():

    openai.api_key = "key de openai"

    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Contexto del asistente
    context = {"role": "system",
               "content": "Eres un asistente muy útil."}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("🆕 Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)


````
````sh
# Salida 
💬 ChatGPT API en Python
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Comando ┃ Descripción                  ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ exit    │ Salir de la aplicación       │
│ new     │ Crear una nueva conversación │
└─────────┴──────────────────────────────┘

¿Sobre qué quieres hablar? : variables python
>  En Python, una variable es un espacio en la memoria que se utiliza para almacenar un valor. Puedes asignar
un valor a una variable utilizando el operador de asignación "=".

Aquí hay algunos ejemplos de variables en Python:

```
x = 5
y = "Hola"
z = True
```

En este ejemplo, la variable "x" se ha asignado con el valor entero 5, la variable "y" se ha asignado con el
valor de cadena "Hola" y la variable "z" se ha asignado con el valor booleano True.

Puedes utilizar operaciones y funciones con variables para realizar cálculos y manipulaciones de datos. Por
ejemplo:

```
x = 10
y = 5
suma = x + y
```

En este ejemplo, se están utilizando las variables "x" y "y" para realizar una suma y almacenar el resultado
en la variable "suma".

Las variables en Python son flexibles y pueden cambiar de tipo de dato. Por ejemplo:

```
x = 5
x = "Hola"
```

En este ejemplo, la variable "x" se ha cambiado de un entero a una cadena.

Es importante tener en cuenta que al utilizar variables, debes ser consciente de los tipos de datos y
asegurarte de utilizarlos adecuadamente en tu código.

¿Sobre qué quieres hablar? : exit
✋ ¿Estás seguro? [y/N]: y
👋 ¡Hasta luego!
Aborted.
````

<br>
<br>

🎉 Enhorabuena has superado el curso. Lo que significa que has alcanzado los conocimientos básicos en Python. 🎉

<br>

[<< 29 Bases datos MYSQL](../29_MYSQL_Python) 

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)


