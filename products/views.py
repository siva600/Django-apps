from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
# Create your views here.
from products.models import Product
from products.forms import RawProductForm


def product_details_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }

    return render(request, 'product_detail.html', context)


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        "form": my_form
    }
    return render(request, 'product_create.html', context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)   # this method is lot easier than try except
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    context = {
        "object": obj
    }
    return render(request, "product_detail.html", context)


def product_delete_view(request,id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('home.html')
    context = {
        "object": obj
    }
    return render(request, "product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'objects': queryset
    }
    return render(request, "product_list.html", context)