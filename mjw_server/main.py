from os import path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from faker import Faker
from .path import getRootPath

app = FastAPI()
faker = Faker()
templates = Jinja2Templates(directory=path.join(getRootPath(), "templates"))
app.mount("/public", StaticFiles(directory=path.join(getRootPath(), "public")), name="public")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": { "title": "MJW Server app" }})

@app.get("/faker")
def call_faker():
  return "fake name ====> %s" % faker.name()
