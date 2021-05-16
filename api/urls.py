from django.urls import path, include
from rest_framework import routers
from .views import AutocompleteViewSet, BranchesViewSet

autocomplete_router = routers.DefaultRouter()
autocomplete_router.register('', AutocompleteViewSet)

branches_router = routers.DefaultRouter()
branches_router.register('', BranchesViewSet)

urlpatterns = [
    path('autocomplete/', include(autocomplete_router.urls)),
    path('', include(branches_router.urls)),
]
