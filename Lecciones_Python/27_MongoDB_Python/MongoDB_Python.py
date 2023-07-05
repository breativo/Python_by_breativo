from fastapi import FastAPI
from routers.user import user


app =FastAPI(
    title="MongoDB in Python",
    description="Aprende a trabajar con MongoDB desde Python",
    version='0.0.1'
)

app.include_router(user)