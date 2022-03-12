from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app import models
from typing import List, Union
from pydantic import UUID4

class DBCrud(ABC):
    model: models.Base
    db: Session

    def save(self, obj: models.Base) -> models.Base:
        self.db.add(obj)
        self.db.commit()
        return obj

    def save_all(self, objs: List[models.Base]):
        self.db.add_all(objs)
        self.db.commit()

    @abstractmethod
    def create(self, *args, **kwargs) -> models.Base:
        return self.save(self.model(*args, **kwargs))

    @abstractmethod
    def get_by_id(self, id: Union[str, UUID4, int]) -> models.Base:
        return self.db.query(self.model).filter(self.model.id == id).first()

    @abstractmethod
    def get_all(self, limit: int = 0) -> List[models.Base]:
        if limit:
            return self.db.query(self.model).limit(limit).all()
        else:
            return self.db.query(self.model).all()

    @abstractmethod
    def delete_by_id(self, id: Union[str, int]) -> models.Base:
        return self.db.query(self.model).filter(self.model.id == id).delete()

    @abstractmethod
    def update(self, id: Union[str, int], *args, **kwargs) -> models.Base:
        return self.db.query(self.model).filter(self.model.id == id).update(*args, **kwargs)

