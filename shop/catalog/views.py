from django.shortcuts import render
from django.views.generic import *
from .models import *


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class ProductListView(ListView):
    template_name = "product/product_list.html"
    model = Product
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.all().prefetch_related("images")


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Product.objects.prefetch_related("images")
