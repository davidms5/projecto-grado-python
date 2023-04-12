from django.urls import path
from .views import ArticuloList, ArticuloDetail

urlpatterns = [
    path('articulos/', ArticuloList.as_view()),
    path('articulos/<int:pk>/', ArticuloDetail.as_view()),
]
