from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'api'

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet, basename='recipe')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'users', views.UserViewSet, basename='users')
router.register(
    r'ingredients', views.IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('djoser.urls.authtoken')),
]