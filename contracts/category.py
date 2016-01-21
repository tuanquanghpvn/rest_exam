from typing import Optional


class Category(object):
    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None,
                 slug: Optional[str] = None):
        self.id = id
        self.name = name
        self.slug = slug


class GetCategoryRequest(Category):
    def __init__(self, id: Optional[int]):
        super().__init__(id=id)


class PostCategoryRequest(Category):
    def __init__(self, name: Optional[str] = None,
                 slug: Optional[str] = None):
        super().__init__(name=name, slug=slug)
