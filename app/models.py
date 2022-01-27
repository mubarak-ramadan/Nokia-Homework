from operator import index
from sqlite3 import IntegrityError
import sqlalchemy as _sql
import database as _database


class Meal(_database.Base):
    __tablename__ = "meals"

    id = _sql.Column(_sql.Integer, primary_key=True, unique=True)
    name = _sql.Column(_sql.String, index=True, nullable=False, unique=True)
    price = _sql.Column(_sql.Float, nullable=False)
    ingredients = _sql.Column(_sql.Text, index=True)
    spicy = _sql.Column(_sql.Boolean, index=True, default=False)
    vegan = _sql.Column(_sql.Boolean, index=True, default=False)
    gluten = _sql.Column(_sql.Boolean, index=True, default=False)
    description = _sql.Column(_sql.Text, index=True)
    kcal = _sql.Column(_sql.Float)
    picture = _sql.Column(_sql.String)    




