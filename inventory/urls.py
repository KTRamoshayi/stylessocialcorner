from django.urls import path
from .views import *

app_name = 'inventory'

urlpatterns = [
    path('category/create', CreateCategory.as_view(), name='create-category'),
    path('category/list', ListCategory.as_view(), name='category-list'),
    path('category/details/<int:pk>', DetailCategory.as_view(), name='category-detail'),
    path('category/update/<int:pk>', UpdateCategory.as_view(), name='category-update'),
    path('category/delete/<int:pk>', DeleteCategory.as_view(), name='category-update'),
    path('categories', ManageCategories.as_view(), name='MCategories')
]
