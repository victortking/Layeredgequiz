from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.edgenosquiz_view, name='edgenosquiz'),
]