from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BrandListView, BrandDetailView, ModelDetailView

urlpatterns = [
    path('', BrandListView.as_view(), name='index'),
    path('brands/<slug:slug>/', BrandDetailView.as_view(), name='phone_model'),
    path('models/<slug:slug>/', ModelDetailView.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
