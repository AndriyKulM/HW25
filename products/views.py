from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .models import Category


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/add.html")
        else:
            product = Product()
            product.title = request.POST.get("title")
            product.description = request.POST.get("description")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def add_category(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "GET":
            return render(request, "products/add_category.html")
        else:
            category = Category()
            category.category_name = request.POST.get("category_name")
            category.save()
            return redirect("/")
    else:
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product, "product_categories": product.categories.all()})


def show_products(request):
    category = request.GET.get("category")

    if category == None:
        products_list = Product.objects.order_by('-title')
    else:
        products_list = Product.objects.filter(categories__category_name=category)

    categories_list = Category.objects.all()

    context = {
        'products': products_list,
        'categories': categories_list
    }

    return render(request, "products/show_products.html", context)