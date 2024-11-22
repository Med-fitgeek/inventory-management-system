from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate
import crud.crud_product as crud_product
from database import get_db
import schemas

router = APIRouter(prefix='/products', tags=['Products'])


@router.get('', response_model=Page[schemas.Product])
def get_products(db: Session = Depends(get_db), category_id: list = Query([])):
    products = crud_product.get_products(db, category_id)
    return paginate(products)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.Product)
def create_product(product_create: schemas.CreateProduct, db: Session = Depends(get_db)):
    try:
        product = crud_product.create_product(db, product_create)
        return product
    except ValueError as e:
        return JSONResponse(status_code=400, content={"message": str(e)})


@router.put('/{product_id}', status_code=status.HTTP_200_OK, response_model=schemas.Product)
def update_product(product_id: str, product_data: schemas.ProductBase, db: Session = Depends(get_db)):
    try:
        updated_product = crud_product.update_product(db, product_id, product_data)
        return updated_product
    except ValueError as e:
        return JSONResponse(status_code=404, content={"message": str(e)})


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: str, db: Session = Depends(get_db)):
    try:
        crud_product.delete_product(db, product_id)
        return None
    except ValueError as e:
        return JSONResponse(status_code=404, content={"message": str(e)})
