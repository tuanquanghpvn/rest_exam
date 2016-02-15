from typing import Optional

# INIT FIELDS
ID = 'id'
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
