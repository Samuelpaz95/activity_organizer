from typing import Optional
from pydantic import BaseModel, Field
from pydantic.main import ModelMetaclass
import pydantic


class PaginateItems(BaseModel):
    next_page: str = Field(..., title="Next page")
    previous_page: str = Field(..., title="Previous page")


class Partial(ModelMetaclass):

    def __new__(self, name, bases, namespaces, **kwargs):
        annotations = namespaces.get('__annotations__', {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith('__'):
                annotations[field] = Optional[annotations[field]]
        namespaces['__annotations__'] = annotations
        return super().__new__(self, name, bases, namespaces, **kwargs)
