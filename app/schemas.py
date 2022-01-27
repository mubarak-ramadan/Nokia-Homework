import pydantic as _pydantic


class _Meal(_pydantic.BaseModel):
    id : int
    name : str
    price : float
    ingredients: str
    spicy : bool
    vegan : bool
    gluten : bool
    description : str
    kcal : float
    picture : str

    class Config:
        orm_mode = True



class CreateMeal(_Meal):
    pass