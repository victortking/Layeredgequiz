from django.urls import path
from . import views

urlpatterns = [
    path('', views.edgenosquiz_view, name='edgenosquiz'),
]