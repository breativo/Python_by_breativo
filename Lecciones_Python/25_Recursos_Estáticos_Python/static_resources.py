'''

API

'''


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

# Img
app.mount('/static', StaticFiles(directory="static"), name="static")


#PDF
app.mount('/pdfs', StaticFiles(directory="static"), name="pdfs")

