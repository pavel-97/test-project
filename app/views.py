from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Products
# Create your views here.

def index(request, page=1):
	args={}
	products=Products.objects.all()
	pages=Paginator(products, 8)
	args['page_range']=pages.page_range
	args['products']=pages.get_page(page)
	args['new']=products[products.count()-3:products.count()]
	return render(request, 'app/index.html', args)

def product_views(request, slug):
	args={}
	
	return render(request, 'app/product.html', args)