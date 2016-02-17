from typing import Optional
from contracts.exeptions import ResourceNotFoundException
from apps.category.models import Category


class CategoryRepository(object):
    @classmethod
    def get_category(cls, limit: Optional[int] = None,
                     offset: Optional[int] = None,
                     sort: Optional[str] = None) -> list:
        try:
            total_count = Category.objects.count()
            if sort:
                results = Category.objects.order_by(sort)[offset:limit]
            else:
                results = Category.objects.order_by("-id")[offset:limit]
            return results, total_count
        except Exception as e:
            raise e

    @classmethod
    def find_category(cls, id: int):
        try:
            category = Category.objects.get(id=id)
            if category:
                return category
            else:
                raise ResourceNotFoundException
        except Exception as e:
            raise e

    @classmethod
    def post_category(cls, name: str, slug: str) -> object:
        try:
            category = Category.objects.create(name=name, slug=slug)
            if category:
                return category
            else:
                raise ResourceNotFoundException
        except Exception as e:
            raise e

    @classmethod
    def put_category(cls, id: int, name: str, slug: str) -> int:
        try:
            category = Category.objects.filter(id=id)
            if not category:
                raise ResourceNotFoundException
            update_count = category.update(
                name=name,
                slug=slug
            )
            if update_count:
                return Category.objects.get(id=id)
        except Exception as e:
            raise e

    @classmethod
    def delete_category(cls, id: int) -> int:
        try:
            category = Category.objects.filter(id=id)
            if category:
                delete_count = category.delete()
                return delete_count
            else:
                raise ResourceNotFoundException
        except Exception as e:
            raise e
