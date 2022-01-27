import database as _database
import models as _models
import schemas as _schemas
from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Session

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def _create_table():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



async def create_meal(meal: _schemas.CreateMeal, db: Session) -> _schemas._Meal:
    meal = _models.Meal(**meal.dict())
    db.add(meal)
    db.commit()
    db.refresh(meal)
    return _schemas._Meal.from_orm(meal)


async def get_meals(db : Session) -> List[_schemas._Meal]:
    meals = db.query(_models.Meal).all()
    return list(map(_schemas._Meal.from_orm, meals))

async def get_a_meal(meal_id: int , db : Session) -> _schemas._Meal:
    meal = db.query(_models.Meal).filter(_models.Meal.id == meal_id).first()
    return meal

async def delete_a_meal(meal: _models.Meal, db : Session):
    db.delete(meal)
    db.commit()

async def update_meal(meal_data : _schemas.CreateMeal, meal : _models.Meal, db = Session) -> _schemas._Meal:
    
    meal.name = meal_data.name
    meal.price = meal_data.price
    meal.ingredients = meal_data.ingredients
    meal.spicy = meal_data.spicy
    meal.vegan = meal_data.vegan
    meal.gluten = meal_data.gluten
    meal.description = meal_data.description
    meal.kcal = meal_data.kcal
    meal.picture = meal_data.picture

    db.commit()
    db.refresh(meal)

    return _schemas._Meal.from_orm(meal)
