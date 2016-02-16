from typing import Optional
from apps.category.models import Category


class CategoryRepository(object):
    @classmethod
    def get_category(cls, limit: Optional[int] = None,
                     offset: Optional[int] = None,
                     sort: Optional[str] = None) -> list:
        if sort:
            results = Category.objects.order_by(sort)[offset:limit]
        else:
            results = Category.objects.order_by("-id")[offset:limit]
        return results, Category.objects.count()

    @classmethod
    def post_category(cls, name: str, slug: str) -> object:
        category = Category.objects.create(name=name, slug=slug)
        return category

    @classmethod
    def put_category(cls, id: int, name: str, slug: str) -> int:
        category = Category.objects.filter(id=id).update(
            name=name,
            slug=slug
        )
        return category

    @classmethod
    def delete_category(cls, id: int) -> int:
        category = Category.objects.filter(id=id).delete()
        return category
