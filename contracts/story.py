from typing import Optional
from .base import (PagingRequest, PagingResponse, DEFAULT_LIMIT, DEFAULT_OFFSET)

# INIT FIELDS
STORY_ID = 'id'
CATEGORY_ID = 'category_id'
NAME = 'name'
SLUG = 'slug'
DESCRIPTION = 'description'
CONTENT = 'content'


class Story(object):
    def __init__(self,
                 id: Optional[int] = None,
                 category_id: Optional[int] = None,
                 name: Optional[str] = None,
                 slug: Optional[str] = None,
                 description: Optional[str] = None,
                 content: Optional[str] = None):
        self.id = id
        self.category_id = category_id
        self.name = name
        self.slug = slug
        self.description = description
        self.content = content


# Request

class GetStoryRequest(PagingRequest):
    def __init__(self, limit: Optional[int] = DEFAULT_LIMIT, offset: Optional[int] = DEFAULT_OFFSET,
                 sort: Optional[str] = None, category_id: Optional[int] = None):
        super().__init__(limit=limit, offset=offset, sort=sort)
        self.category_id = category_id


class DetailStoryRequest(Story):
    def __init__(self, id: Optional[int] = None):
        super().__init__(id=id)


class PostStoryRequest(Story):
    def __init__(self,
                 category_id: Optional[int] = None,
                 name: Optional[str] = None,
                 slug: Optional[str] = None,
                 description: Optional[str] = None,
                 content: Optional[str] = None):
        super().__init__(category_id=category_id, name=name,
                         slug=slug, description=description, content=content)


class PutStoryRequest(Story):
    def __init__(self,
                 id: Optional[int] = None,
                 category_id: Optional[int] = None,
                 name: Optional[str] = None,
                 slug: Optional[str] = None,
                 description: Optional[str] = None,
                 content: Optional[str] = None):
        super().__init__(id=id, category_id=category_id, name=name,
                         slug=slug, description=description, content=content)


class DeleteStoryRequest(Story):
    def __init__(self, id: Optional[int] = None):
        super().__init__(id=id)


# Response

class GetStoryResponse(PagingResponse):
    def __init__(self, request: PagingRequest, response: list, path: str, total_count: int):
        super().__init__(request_obj=request, path=path, count=len(response), total_count=total_count)
        self.results = response


class DetailStoryResponse(Story):
    def __init__(self, id: int, category_id: int, name: str, slug: str, description: Optional[str], content: str,
                 **kwargs):
        super().__init__(id=id, category_id=category_id, name=name, slug=slug, description=description, content=content)


class PostStoryResponse(Story):
    def __init__(self, id: int, category_id: int, name: str, slug: str, description: Optional[str], content: str,
                 **kwargs):
        super().__init__(id=id, category_id=category_id, name=name, slug=slug, description=description, content=content)


class PutStoryResponse(Story):
    def __init__(self, id: int, category_id: int, name: str, slug: str, description: Optional[str], content: str,
                 **kwargs):
        super().__init__(id=id, category_id=category_id, name=name, slug=slug, description=description, content=content)


class DeleteStoryResponse(Story):
    def __init__(self, id: int):
        super().__init__(id=id)
