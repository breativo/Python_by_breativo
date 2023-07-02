# Recursos estáticos Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 25. Recursos estáticos.
<h2 style="color:#15A7E1">Recursos estáticos.</h2>
Dentro de FastAPI, el objeto StaticFiles se utiliza para servir archivos estáticos, como archivos HTML, CSS, JavaScript, imágenes u otros recursos estáticos, desde un directorio específico en tu servidor.

El uso de StaticFiles te permite configurar una ruta en tu API para servir archivos estáticos de manera eficiente y conveniente. Puedes utilizarlo para servir archivos estáticos relacionados con la interfaz de usuario de tu aplicación web. Una vez configurado, cualquier archivo que esté presente en el directorio "static" podrá ser accedido desde la ruta "/static". 

Es importante tener en cuenta que el directorio especificado en directory debe ser una ruta absoluta o una ruta relativa al directorio de trabajo actual. Además, ten en cuenta la seguridad y asegúrate de que solo se sirvan archivos estáticos que desees compartir públicamente.

El uso de StaticFiles en FastAPI es una forma sencilla de servir archivos estáticos en tu aplicación web, lo que facilita la creación de interfaces de usuario interactivas y atractivas.
<br>
<br>

````py
# Entrada
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

````

<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 24 Routers](../24_Routers_Python) | [26 Aitorización >>](../26_Autorización_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)

