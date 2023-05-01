from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="brands", null=True)
    origin = models.CharField(max_length=50)
    manufacturing_date = models.DateField()
    slug = models.SlugField(max_length=150, default='null')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PhoneReview:phone_model", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="models", null=True)
    launch_date = models.DateField()
    platform = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, default='null')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PhoneReview:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Review(models.Model):
    article = models.TextField()
    date_published = models.DateTimeField(auto_now=True)
    model = models.ManyToManyField(Model)

    def get_absolute_url(self):
        related_model = self.model.first()
        return reverse("PhoneReview:detail", kwargs={"slug": related_model.slug})
