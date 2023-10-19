from django.urls import path
from .views import ProductList, LessonList, LessonViewList

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('lessons/', LessonList.as_view(), name='lesson-list'),
    path('lesson-views/', LessonViewList.as_view(), name='lesson-view-list'),
]
