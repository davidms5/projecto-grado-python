from django.urls import path
from .views import ArticuloList, ArticuloDetail, CreateUser, download_pdf

urlpatterns = [
    path('tickets/', ArticuloList.as_view()),
    path('tickets/<uuid:pk>/', ArticuloDetail.as_view()),
    path('tickets/<uuid:pk>/download-pdf/', download_pdf),
    path('tickets/empleados/', CreateUser.as_view()),
]
