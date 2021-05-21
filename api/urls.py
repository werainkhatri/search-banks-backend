from django.urls import path, include
from rest_framework import routers
from .views import AutocompleteViewSet, BranchesViewSet, IFSCViewSet

autocomplete_router = routers.DefaultRouter()
autocomplete_router.register('', AutocompleteViewSet)

branches_router = routers.DefaultRouter()
branches_router.register('', BranchesViewSet)

ifsc_router = routers.DefaultRouter()
ifsc_router.register('', IFSCViewSet)

urlpatterns = [
    path('branches/autocomplete/', include(autocomplete_router.urls)),
    path('branches/', include(branches_router.urls)),
    path('ifsc/', include(ifsc_router.urls)),
]
