from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud.crud_category as crud_category
from database import get_db
import schemas

router = APIRouter(prefix='/categories', tags=['Categories'])


@router.get('', response_model=list[schemas.Category])
def get_categories(db: Session = Depends(get_db)):
    return crud_category.get_categories(db)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.Category)
def create_category(category_create: schemas.CreateCategory, db: Session = Depends(get_db)):
    try:
        new_category = crud_category.create_category(db, category_create)
        return new_category
    except ValueError as e:
        return JSONResponse(status_code=400, content={"message": str(e)})