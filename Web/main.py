# pip install reactpy
# pip install uvicorn

from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def HelloWorld():
    return html.div(
        html.h1("LISTA"),
        html.ul(
            html.li("cosa1"),
            html.li("cosa2"),
        )
    )

app = FastAPI()
configure(app, HelloWorld)