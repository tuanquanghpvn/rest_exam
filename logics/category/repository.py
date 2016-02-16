from typing import Optional
from apps.category.models import Category


class CategoryRepository(object):
    @classmethod
    def get_category(cls,
                     limit: Optional[int] = None,
                     offset: Optional[int] = None,
                     sort: Optional[str] = None) -> list:
        results = Category.objects.all()
        return results