from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='index'),
    # path('', views.index_view, name='index'),
]
