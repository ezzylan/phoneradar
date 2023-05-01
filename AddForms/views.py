from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from PhoneReview.models import Brand, Model, Review
from .forms import BrandForm, ModelForm, ReviewForm


class BrandCreateView(LoginRequiredMixin, CreateView):
    template_name = "AddForms/add_brand_form.html"
    model = Brand
    form_class = BrandForm


class ModelCreateView(LoginRequiredMixin, CreateView):
    template_name = "AddForms/add_model_form.html"
    model = Model
    form_class = ModelForm


class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = "AddForms/add_review_form.html"
    model = Review
    form_class = ReviewForm


# class AddBrandFormView(TemplateView):
#     template_name = "AddForms/add_brand_form.html"

#     def get(self, request):
#         form = BrandForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = BrandForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('PhoneReview:index'))

#         return render(request, self.template_name, {'form': form})


# class AddModelFormView(TemplateView):
#     template_name = "AddForms/add_model_form.html"

#     def get(self, request):
#         form = ModelForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = ModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('PhoneReview:index'))

#         return render(request, self.template_name, {'form': form})


# class AddReviewFormView(TemplateView):
#     template_name = "AddForms/add_review_form.html"

#     def get(self, request):
#         form = ReviewForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('PhoneReview:index'))

#         return render(request, self.template_name, {'form': form})
