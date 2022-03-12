from .base import DBCrud
from sqlalchemy.orm import Session
from typing import Optional, List, Any, Union
from pydantic import UUID4
from app import schemas, core, models
from app.core import auth

class UserCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.User

    def create(self, user: schemas.UserCreate) -> models.User:
        return self.save(self.model(full_name = user.full_name,
                                    phone_number = user.phone_number,
                                    email = user.email,
                                    hashed_password = core.AuthManager.get_password_hash(user.password),
                                    account_id = user.account_id,
                                    ))

    def get_by_id(self, id: Union[str, UUID4]) -> Optional[models.User]:
        return super().get_by_id(id)

    def get_by_name(self, name: str) -> Optional[models.User]:
        return self.db.query(self.model).filter(self.model.full_name == name).first()

    def get_by_email(self, email: str) -> Optional[models.User]:
        return self.db.query(self.model).filter(self.model.email == email).first()

    def get_by_account_id(self, account_id: UUID4) -> List[models.User]:
        return self.db.query(self.model).filter(self.model.account_id == account_id).all()

    def get_all(self, limit: int = 0) -> List[models.User]:
        return super().get_all(limit)

    def delete_by_id(self, id: Union[str, int]) -> models.User:
        return super().delete_by_id(id)

    def delete_by_name(self, name: str) -> Any:
        return self.db.query(self.model).filter(self.model.full_name == name).delete()

    def update(self, id: str, user: schemas.UserUpdate) -> models.User:
        return super().update(id, user.dict())

    def authenticate(self, email: str, password: str) -> Optional[models.User]:
        user = self.get_by_email(email)
        if user and auth.verify_password(password, user.hashed_password):
            return user
