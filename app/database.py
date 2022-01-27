import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# DATABASE_URL ="postgresql://postgres:password@localhost:5432/postgres"
DATABASE_URL ="postgresql://new_user:password@db:5432/meal_db"

engine = _sql.create_engine(DATABASE_URL, echo=False)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()

 
# command: bash -c "alembic upgrade head"
