from django.urls import path, include
from rest_framework import routers
from .views import AutocompleteViewSet, BranchesViewSet, BankViewSet

autocomplete_router = routers.DefaultRouter()
autocomplete_router.register('', AutocompleteViewSet)

branches_router = routers.DefaultRouter()
branches_router.register('', BranchesViewSet)

banks_router = routers.DefaultRouter()
banks_router.register('', BankViewSet)

urlpatterns = [
    path('branches/autocomplete/', include(autocomplete_router.urls)),
    path('branches/', include(branches_router.urls)),
    path('banks/', include(banks_router.urls)),
]
