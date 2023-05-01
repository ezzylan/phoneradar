from django import forms
from PhoneReview.models import Brand, Model, Review


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        exclude = ["slug"]


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        exclude = ["slug"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
