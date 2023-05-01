from django.views.generic import ListView, DetailView
from .models import Brand, Model, Review

# Create your views here.


class BrandListView(ListView):
    template_name = "PhoneReview/index.html"
    context_object_name = "all_brands"

    def get_queryset(self):
        return Brand.objects.all()


class BrandDetailView(DetailView):
    model = Brand
    template_name = "PhoneReview/phone_model.html"
    context_object_name = "brand"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = Model.objects.filter(brand=self.object)
        return context


class ModelDetailView(DetailView):
    model = Model
    template_name = "PhoneReview/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(model=self.object)
        return context
