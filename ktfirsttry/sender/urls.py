from django.urls import path

from .views import index
from .views import SndCreateView, SingleSndAPIView, SndAPICreateView
from . import views




urlpatterns = [
    path('', index, name='index'),
    path('add/', SndCreateView.as_view(), name='add'),
    path('api/', SndAPICreateView.as_view()),
    path('api/<int:pk>', SingleSndAPIView.as_view()),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>', views.delete, name='delete'),
]
