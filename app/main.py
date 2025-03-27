from fastapi import FastAPI, APIRouter
from enum import Enum
from pydantic import BaseModel
from .dependencies import get_query_token, get_token_header
from .routers import restauraunt

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

router = FastAPI()
router.include_router(restauraunt.router)
# router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@router.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
