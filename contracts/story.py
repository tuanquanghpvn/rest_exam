from typing import Optional

# INIT FIELDS
ID = 'id'
ID_CATEGORY = 'id_category'
NAME = 'name'
SLUG = 'slug'
DESCRIPTION = 'description'
CONTENT = 'content'


class Story(object):
    def __init__(self,
                 id: Optional[int] = None,
                 id_category: Optional[int] = None,
                 name: Optional[str] = None,
                 slug: Optional[str] = None,
                 description: Optional[str] = None,
                 content: Optional[str] = None):
        self.id = id
        self.id_category = id_category
        self.name = name
        self.slug = slug
        self.description = description
        self.content = content


# Request

class PostStoryRequest(Story):
    def __init__(self,
                 id_category: Optional[int] = None,
                 name: Optional[str] = None,
                 slug: Optional[str] = None,
                 description: Optional[str] = None,
                 content: Optional[str] = None):
        super().__init__(id_category=id_category, name=name,
                         slug=slug, description=description, content=content)


class PutStoryRequest(Story):
    def __init__(self,
                 id: Optional[int] = None,
                 id_category: Optional[int] = None,
                 name: Optional[str] = None,
                 slug: Optional[str] = None,
                 description: Optional[str] = None,
                 content: Optional[str] = None):
        super().__init__(id=id, id_category=id_category, name=name,
                         slug=slug, description=description, content=content)


class DeleteStoryRequest(Story):
    def __init__(self, id: Optional[int] = None):
        super().__init__(id=id)


# Response
