from typing import Optional
from contracts.base import (PagingRequest, PagingResponse, DEFAULT_LIMIT, DEFAULT_OFFSET)

# INIT FIELDS
CATEGORY_ID = 'id'
NAME = 'name'
SLUG = 'slug'


class Category(object):
    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None,
                 slug: Optional[str] = None):
        self.id = id
        self.name = name
        self.slug = slug


# Request

class GetCategoryRequest(PagingRequest):
    def __init__(self,
                 limit: int = DEFAULT_LIMIT,
                 offset: int = DEFAULT_OFFSET,
                 sort: Optional[str] = None):
        super().__init__(limit=limit, offset=offset, sort=sort)


class PostCategoryRequest(Category):
    def __init__(self,
                 name: Optional[str] = None,
                 slug: Optional[str] = None):
        super().__init__(name=name, slug=slug)


class PutCategoryRequest(Category):
    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None,
                 slug: Optional[str] = None):
        super().__init__(id, name, slug)


class DeleteCategoryRequest(Category):
    def __init__(self,
                 id: Optional[int] = None):
        super().__init__(id)


# Response

class GetCategoryResponse(PagingResponse):
    def __init__(self,
                 request: PagingRequest,
                 path: str,
                 category_list: list):
        super().__init__(request_obj=request, path=path, count=len(category_list))


class PostCategoryResponse(Category):
    def __init__(self,
                 id: int,
                 name: str,
                 slug: str):
        super().__init__(id=id, name=name, slug=slug)


class PutCategoryResponse(Category):
    def __init__(self,
                 id: int,
                 name: str,
                 slug: str):
        super().__init__(id=id, name=name, slug=slug)


class DeleteCategoryResponse(Category):
    def __init__(self, id: int):
        super().__init__(id=id)