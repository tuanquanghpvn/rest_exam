from typing import Optional

from django.db import transaction
from sqlalchemy import func
from sqlalchemy.util import KeyedTuple
from sqlalchemy.orm.exc import NoResultFound

from contracts.exeptions import ResourceNotFoundException
from apps.category.models import Category
from apps.story.models import Story
from contracts.story import (STORY_ID, NAME, SLUG, DESCRIPTION, CONTENT, CATEGORY_ID)
from logics.base.respository import BaseRespository

STORY_LABEL = [STORY_ID, NAME, SLUG, DESCRIPTION, CONTENT, CATEGORY_ID]


class StoryRespository(object):
    @classmethod
    def get_story(cls, limit: Optional[int] = None,
                  offset: Optional[int] = None,
                  sort: Optional[str] = None,
                  category_id: Optional[int] = None) -> list:
        story_qs = Story.sa.query(
            Story.sa.id,
            Story.sa.name,
            Story.sa.slug,
            Story.sa.description,
            Story.sa.content,
            Category.sa.name.label('category_name')
        ).join(
            Category.sa
        )
        if category_id:
            total_count = Story.sa.query(func.count(Story.sa.id)).filter(Category.sa.id == category_id).scalar()
            story_qs = story_qs.filter(
                Category.sa.id == category_id
            )
        else:
            total_count = Story.sa.query(func.count(Story.sa.id)).scalar()
        story_qs = BaseRespository.filter_limit(story_qs, limit)
        story_qs = BaseRespository.filter_offset(story_qs, offset)
        story_qs = BaseRespository.sort_all(story_qs, sort, Story)
        try:
            result = story_qs.all()
        except NoResultFound:
            result = None
        return result, total_count

    @classmethod
    def detail_story(cls, id: int) -> Optional[KeyedTuple]:
        story_qs = Story.sa.query(
            Story.sa.id,
            Story.sa.name,
            Story.sa.slug,
            Story.sa.description,
            Story.sa.content,
            Category.sa.name.label('category_name')
        ).join(
            Category.sa
        )
        story_qs = story_qs.filter(
            Story.sa.id == id
        )
        try:
            story = story_qs.one()
            result = KeyedTuple(
                [story.id, story.name, story.slug, story.description, story.content, story.category_name],
                labels=STORY_LABEL)
        except NoResultFound:
            result = None
        return result

    @classmethod
    def post_story(cls, category_id: int, name: str, slug: str,
                   description: Optional[str], content: str) -> Optional[KeyedTuple]:
        with transaction.atomic():
            story = Story.objects.create(category__id=category_id, name=name, slug=slug,
                                         description=description, content=content)
        try:
            result = KeyedTuple(
                [story.id, story.name, story.slug, story.description, story.content, story.category_name],
                labels=STORY_LABEL)
        except Exception as exc:
            result = None
        return result

    @classmethod
    def put_story(cls, id: int, category_id: int, name: str, slug: str,
                  description: Optional[str], content: str):
        try:
            category = Category.objects.filter(id=category_id)
            story = Story.objects.filter(id=id)
            if not category or not story:
                return None
            update_count = story.update(category_id=category_id, name=name, slug=slug,
                                        description=description, content=content)
            if update_count:
                return cls.detail_story(id=id)
        except Exception as exc:
            return None

    @classmethod
    def delete_story(cls, id: int):
        try:
            story = Story.objects.filter(id=id)
            if story:
                delete_count = story.delete()
                return delete_count
            else:
                return None
        except Exception as e:
            return None
