from django.urls import path
from .views import BrandCreateView, ModelCreateView, ReviewCreateView

urlpatterns = [
    path('brand/', BrandCreateView.as_view(), name='addbrand'),
    path('model/', ModelCreateView.as_view(), name='addmodel'),
    path('review/', ReviewCreateView.as_view(), name='addreview'),
]
