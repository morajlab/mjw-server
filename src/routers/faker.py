from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import JSONResponse
from faker import Faker

faker = Faker()
router = APIRouter()
app = FastAPI()

class FakerAttributeException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(FakerAttributeException)
async def faker_attribute_exception_handler(request: Request, exc: FakerAttributeException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Provider/Function '{exc.name}' doesn't exists."},
    )

@router.get("/faker/{provider}/{function}")
def call_faker(provider, function):
  try:
    value = getattr(faker, function)()

    return JSONResponse(content={"value": value})
  except AttributeError:
    raise FakerAttributeException(name=f"{provider}/{function}") from None
  except Exception as ex:
    raise ex

@router.get("/faker/providers")
def get_providers():
  return JSONResponse(content={ "providers": [p.__provider__.split(".")[-1] for p in faker.providers] })

@router.get("/faker/locales")
def get_locales():
  print(faker.locales)
  return JSONResponse(content={ "locales": faker.locales })
