from django.urls import path
from .views import ArticuloList, ArticuloDetail, CreateUser

urlpatterns = [
    path('tickets/', ArticuloList.as_view()),
    path('tickets/<str:pk>/', ArticuloDetail.as_view()),
    path('tickets/empleados/', CreateUser.as_view()),
]
