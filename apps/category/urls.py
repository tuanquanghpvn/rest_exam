from django.conf.urls import include, url
from .views import CategoryView


urlpatterns = [
    url(r'^$', CategoryView.as_view()),
]