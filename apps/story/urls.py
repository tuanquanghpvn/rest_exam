from django.conf.urls import url
from .views import (StorysView, StoryView)


urlpatterns = [
    url(r'^$', StorysView.as_view()),
    url(r'^(?P<code>[0-9]+)$', StoryView.as_view()),
]