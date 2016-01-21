from typing import Optional


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