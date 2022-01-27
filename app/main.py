from fastapi import FastAPI, Depends
from starlette.exceptions import HTTPException
from pydoc import apropos
import database as _database
from typing import TYPE_CHECKING, List
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services
import models as _models
from database import engine, Base


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

_database.Base.metadata.create_all(bind=_database.engine)

app = FastAPI()


@app.get('/')
def home():
    return {"Welcome" : "Meals diary"}

@app.post("/meals", response_model=_schemas._Meal)
async def create_meal(
    meal: _schemas.CreateMeal,
    db:  _orm.Session = Depends(_services.get_db),
    ):
    return await _services.create_meal(meal=meal, db=db)


@app.get("/meals", response_model=List[_schemas._Meal])
async def get_meals(
    db:  _orm.Session = Depends(_services.get_db)
):
    return await _services.get_meals(db=db)


@app.get("/meal/{meal_id}", response_model=_schemas._Meal)
async def get_meal(meal_id: int , db: _orm.Session = Depends(_services.get_db)):
    meal = await _services.get_a_meal(db=db, meal_id=meal_id)

    if not meal:
        raise HTTPException(status_code=404, detail="Meal does not exist")
    await _services.delete_a_meal(meal, db=db)

    return meal


@app.delete("/meal/{meal_id}")
async def delete_a_meal(meal_id: int , db:  _orm.Session = Depends(_services.get_db)):
    meal = await _services.get_a_meal(db=db, meal_id=meal_id)

    if not meal:
        raise HTTPException(status_code=404, detail="Meal does not exist")
    await _services.delete_a_meal(meal, db=db)

    return "Successfully deleted meal"
    

@app.put("/meal/{meal_id}", response_model=_schemas._Meal)
async def update_meal(
    meal_id: int , 
    meal_data : _schemas.CreateMeal, 
    db: _orm.Session = Depends(_services.get_db)):

    meal = await _services.get_a_meal(db=db, meal_id=meal_id)

    if not meal:
        raise HTTPException(status_code=404, detail="Meal does not exist")
    
    return await _services.update_meal(meal=meal, meal_data=meal_data, db = db)






