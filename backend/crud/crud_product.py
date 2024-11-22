from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import models
import schemas


def get_products(db: Session, category_ids: list = []):
    products = db.query(models.Product).filter(models.Product.active)
    if category_ids:
        products = products.filter(models.Product.category_id.in_(category_ids))
    return products.all()


def create_product(db: Session, product_data: schemas.CreateProduct):
    try:
        new_product = models.Product(**product_data.model_dump())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except IntegrityError:
        raise ValueError("Category does not exist")


def update_product(db: Session, product_id: str, product_data: schemas.ProductBase):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        try:
            data = product_data.model_dump()
            if data['name'] is not None:
                product.name = data['name']
            if data['description'] is not None:
                product.description = data['description']
            if data['price'] is not None:
                product.price = data['price']
            if data['category_id'] is not None:
                product.category_id = data['category_id']
            
            db.commit()
            return product
        except IntegrityError:
            raise ValueError("Category does not exist")
    else:
        raise ValueError("Product does not exist")


def delete_product(db: Session, product_id: str):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        product.active = False
        db.commit()
    else:
        raise ValueError("Product does not exist")
