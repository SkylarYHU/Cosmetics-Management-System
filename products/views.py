from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator

# Create your views here.
def product_list(request):
  search_query = request.GET.get('search', '')
  if search_query:
    product_list = Product.objects.filter(name__icontains=search_query)
  else:
    product_list = Product.objects.all()
  paginator = Paginator(product_list, 10)
  page_number = request.GET.get('page')
  products = paginator.get_page(page_number)
  return render(request, 'products/product_list.html', {"products": products})

def product_detail(request,pk):
  # 如果未找到对象，则返回一个 HTTP 404 错误页面
  # 尝试查找主键为pk的Product 对象
  product = get_object_or_404(Product, pk=pk)
  return render(request, "products/product_detail.html", {"product":product})

def product_create(request):
  if request.method == "POST":
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('product_list')
  else:
    form = ProductForm()
  return render(request, 'products/product_form.html', {'form':form})

def product_update(request,pk):
  product = get_object_or_404(pk=pk)
  if request.method == "POST":
    # instance=product指定要更新的模型实例
    # Django 表单数据应用到这个实例上，而不是创建新的数据库对象
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
      form.save()
      return redirect('product_list')
  else:
    form = ProductForm(instance=product)
  return render(request, 'products/product_form.html', {"form":form})

def product_delete(request,pk):
  product = get_object_or_404(pk=pk)
  if request.method == "POST":
    product.delete()
    return redirect('product_list')
  return render(request, 'products/product_confirm_delete.html', {"product":product})