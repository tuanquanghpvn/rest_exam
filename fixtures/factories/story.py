from apps.story.models import Story
from factory import DjangoModelFactory


class StoryFactory(DjangoModelFactory):
    """
        Story Factory
    """
    class Meta:
        model = Story
