import statistics
from fastapi import Depends, FastAPI, status
from typing import Union, Annotated
import database, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session 


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

MonkTableCreate= Depends(get_db)

@app.post('/monk_table', status_code=201)
async def create_monk_table(monk_table: Session = MonkTableCreate, db: Session = db_dependency):
    db_monk_table = models.MonkTable(**monk_table.model_dump())
    db.add(db_monk_table)
    db.commit()
    db.refresh(db_monk_table)
    return db_monk_table

#@app.get('/Users')
#async def read_root(db: Session = db_dependency):
    #return {"Hello": "World"}


#@app.get('/items')
#async def read_item():
    #return db_dependency.execute(models.MonkTable.select(id=2))
    #return "hello"
