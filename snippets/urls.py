from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

router = DefaultRouter(trailing_slash=False)
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
  path('', include(router.urls))
]