from sqlalchemy.orm import Session
import models
import schemas


def get_categories(db: Session):
    return db.query(models.Category).all()


def create_category(db: Session, category_data: schemas.CreateCategory):
    data = category_data.model_dump()

    if len(data['name']) > 600:
        raise ValueError("Category name is too long")
    if data['name'].isdigit():
        raise ValueError("Category name cannot contain only numbers")

    new_category = models.Category(**data)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category