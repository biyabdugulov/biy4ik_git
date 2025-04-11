from django.db.migrations.state import ProjectState

from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'