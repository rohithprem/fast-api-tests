from fastapi import APIRouter, Depends, HTTPException
from enum import Enum
from app.dependencies import get_token_header
from pydantic import BaseModel
from uuid import uuid4, UUID

router = APIRouter(
    prefix="/restaurants",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

class DrinkEnum(str, Enum):  
    coffee: str = "coffee"  
    soda: str = "soda"  
    beer: str = "beer"  
    wine: str = "wine"  
  
  
class MealEnum(str, Enum):  
    pasta: str = "pasta"  
    pizza: str = "pizza"  
    meat: str = "meat"  
    fish: str = "fish"  
  
  
class DessertEnum(str, Enum):  
    cookie: str = "cookie"  
    donut: str = "donut"  
    brownie: str = "brownie"  
    gelato: str = "gelato"  
  
  
class OrderCreate(BaseModel):  
    order_id: UUID = uuid4()  
    drink: DrinkEnum  
    meal: MealEnum  
    dessert: DessertEnum

@router.post(  
    "",  
    status_code=201,  
    name="create_order",  
)  
def create_order(  
    order_create: OrderCreate, 
):   
    return {"Say": "Order created!"}