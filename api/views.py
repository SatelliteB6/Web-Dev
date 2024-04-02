from django.http import JsonResponse
from .models import Product, Category

def list_products(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    return JsonResponse(data)

def get_product(request, id):
    try:
        product = Product.objects.get(pk=id)
        data = {'product': model_to_dict(product)}
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def list_categories(request):
    categories = Category.objects.all()
    data = {'categories': list(categories.values())}
    return JsonResponse(data)

def get_category(request, id):
    try:
        category = Category.objects.get(pk=id)
        data = {'category': model_to_dict(category)}
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

def list_products_by_category(request, id):
    try:
        category = Category.objects.get(pk=id)
        products = Product.objects.filter(category=category)
        data = {'products': list(products.values())}
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
