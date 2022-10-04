from django.urls import path
from . import views

urlpatterns = [
    path('category_list/',views.CategoryListView.as_view(), name='category_list'),
    path('category_detail/<int:pk>/',views.CategoryDetail.as_view(), name='category_detail'),
    path('category_update/<int:pk>/',views.CategoryUpdate.as_view(), name='category_update'),
    path('category_create/',views.CategoryCreate.as_view(), name='category_create'),
    path('category_updateform/<int:pk>/',views.CategoryFormUpdate.as_view(), name='category_updateform'),
    path('category_delete/<int:pk>/',views.CategoryFormDelete.as_view(), name='category_deleteform'),
]