from typing import Optional
from contracts.exeptions import ResourceNotFoundException
from apps.category.models import Category
from apps.story.models import Story


class StoryRespository(object):
    @classmethod
    def get_story(cls, limit: Optional[int] = None,
                  offset: Optional[int] = None,
                  sort: Optional[str] = None,
                  category_id: Optional[int] = None):
        try:
            if category_id:
                total_count = Story.objects.filter(category__id=category_id).count()
                if sort:
                    results = Story.objects.filter(category__id=category_id).order_by(sort)[offset:limit]
                else:
                    results = Story.objects.filter(category__id=category_id)[offset:limit]
            else:
                total_count = Story.objects.count()
                if sort:
                    results = Story.objects.order_by(sort)[offset:limit]
                else:
                    results = Story.objects.order_by("-id")[offset:limit]
            return results, total_count
        except Exception as e:
            raise e

    @classmethod
    def find_story(cls, id: int):
        try:
            story = Story.objects.get(id=id)
            if story:
                return story
            else:
                raise ResourceNotFoundException
        except Exception as e:
            raise e

    @classmethod
    def post_story(cls, category_id: int, name: str, slug: str,
                      description: Optional[str], content: str):
        try:
            category = Category.objects.get(id=category_id)
            if not category:
                raise ResourceNotFoundException
            story = Story.objects.create(category=category, name=name, slug=slug,
                                         description=description, content=content)
            return story
        except Exception as e:
            raise e

    @classmethod
    def put_story(cls, id: int, category_id: int, name: str, slug: str,
                     description: Optional[str], content: str):
        try:
            category = Category.objects.filter(id=category_id)
            story = Story.objects.filter(id=id)
            if not category or not story:
                raise ResourceNotFoundException
            update_count = story.update(category_id=category_id, name=name, slug=slug,
                                        description=description, content=content)
            if update_count:
                return Story.objects.get(id=id)
        except Exception as e:
            raise e

    @classmethod
    def delete_story(cls, id: int):
        try:
            story = Story.objects.filter(id=id)
            if story:
                delete_count = story.delete()
                return delete_count
            else:
                raise ResourceNotFoundException
        except Exception as e:
            raise e
