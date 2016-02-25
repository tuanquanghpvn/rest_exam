from django.conf.urls import url
from .views import (CategorysView, CategoryView)


urlpatterns = [
    url(r'^$', CategorysView.as_view()),
    url(r'^(?P<code>[0-9]+)/$', CategoryView.as_view()),
]