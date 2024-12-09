from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import ProductForm


# Create
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/AddProduct.html', {'form': form})
