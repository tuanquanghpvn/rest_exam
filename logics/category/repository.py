from typing import Optional
from django.db import transaction
from sqlalchemy import func
from sqlalchemy.util import KeyedTuple
from sqlalchemy.orm.exc import NoResultFound
from apps.category.models import Category
from contracts.category import (CATEGORY_ID, NAME, SLUG)
from logics.base.respository import BaseRespository

CATEGORY_LABEL = [CATEGORY_ID, NAME, SLUG]


class CategoryRepository(object):
    @classmethod
    def get_category(cls, limit: Optional[int] = None,
                     offset: Optional[int] = None,
                     sort: Optional[str] = None) -> list:
        category_qs = Category.sa.query(
            Category.sa.id,
            Category.sa.name,
            Category.sa.slug
        )
        total_count = Category.sa.query(func.count(Category.sa.id)).scalar()
        category_qs = BaseRespository.filter_limit(category_qs, limit)
        category_qs = BaseRespository.filter_offset(category_qs, offset)
        category_qs = BaseRespository.sort_all(category_qs, sort, Category)
        try:
            result = category_qs.all()
        except NoResultFound:
            result = None
        return result, total_count

    @classmethod
    def detail_category(cls, id: int) -> Optional[KeyedTuple]:
        category_qs = Category.sa.query(
            Category.sa.id,
            Category.sa.name,
            Category.sa.slug
        )
        category_qs = category_qs.filter(
            Category.sa.id == id
        )
        try:
            category = category_qs.one()
            result = KeyedTuple([category.id, category.name, category.slug], labels=CATEGORY_LABEL)
        except NoResultFound:
            result = None
        return result

    @classmethod
    def post_category(cls, name: str, slug: str) -> object:
        with transaction.atomic():
            category = Category.objects.create(name=name, slug=slug)
        try:
            result = KeyedTuple([category.id, category.name, category.slug], labels=CATEGORY_LABEL)
        except Exception as exc:
            result = None
        return result

    @classmethod
    def put_category(cls, id: int, name: str, slug: str) -> int:
        update_count = Category.objects.filter(id=id).update(
            name=name,
            slug=slug
        )
        if update_count:
            result = cls.detail_category(id=id)
        else:
            result = None
        return result

    @classmethod
    def delete_category(cls, id: int) -> int:
        delete_count = Category.objects.filter(id=id).delete()
        if delete_count:
            return delete_count
        else:
            return None
