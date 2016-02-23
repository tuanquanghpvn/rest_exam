from apps.category.models import Category
from factory import DjangoModelFactory


class CategoryFactory(DjangoModelFactory):
    """
        Category Factory
    """

    class Meta:
        model = Category
