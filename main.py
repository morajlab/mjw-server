from os import path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from faker import Faker

app = FastAPI()
faker = Faker()
templates = Jinja2Templates(directory=path.dirname(__file__))
app.mount("/static", StaticFiles(directory=path.join(path.dirname(__file__), "static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/faker")
def call_faker():
  return "fake name ====> %s" % faker.name()
