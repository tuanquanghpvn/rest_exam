from django.conf.urls import include, url
from .views import CategoryView


urlpatterns = [
    url(r'^$', CategoryView.as_view()),
    url(r'^(?P<code>[0-9]+)$', CategoryView.as_view()),
]