from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product, Lesson, LessonView
from .serializers import ProductSerializer, LessonSerializer, LessonViewSerializer
from django.http import HttpResponse


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonViewList(generics.ListCreateAPIView):
    queryset = LessonView.objects.all()


def home(request):
    return HttpResponse("Добро пожаловать на домашнюю страницу!")