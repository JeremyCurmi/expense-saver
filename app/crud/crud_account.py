from .base import DBCrud
from sqlalchemy.orm import Session
from typing import Optional, List, Any, Union
from pydantic import UUID4
from app import schemas, models

class AccountCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.Account

    def create(self, account: schemas.AccountCreate) -> models.Account:
        return self.save(self.model(name=account.name,
                                    description=account.description))


    def get_by_id(self, user_id: Union[str, UUID4]) -> Optional[models.Account]:
        return None


    def get_by_name(self, name: str) -> Optional[models.Account]:
        return self.db.query(self.model).filter(self.model.name == name).first()


    def get_all(self, limit: int = 0) -> List[models.Account]:
        return super().get_all(limit)


    def delete_by_id(self, user_id: Union[str, int]) -> Optional[models.Account]:
        return None


    def update(self, id: str) -> Optional[models.Account]:
        return None