from django.urls import path
from .views import create_groups , add_permissions , remove_permissions
urlpatterns = [
    path('create_groups/' , create_groups),
    path('add_permissions/' , add_permissions),
    path('remove_permissions/' , remove_permissions)

]