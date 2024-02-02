from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.paginator import Paginator
from django.db.models import Q

from ..models import Follower, Product, TopCategory, MidCategory, BottomCategory, ProductImage

from ..forms.user_forms import NewsLetterForm 


def index(request):
    """
    Landing Page.
    """
    return render(request, "products/index.html")


def products(request):
    """
    All Products Page.
    """
    is_admin: bool = request.user.is_superuser
    items = Product.objects.all().order_by('-created_at')
    items = [item.check_availabality() for item in items]
    items_per_page = 12
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page, 'is_admin': is_admin}
    return render(request, "products/products.html", context)

    
def about(request): 
    """
    About Page.
    """
    return render(request, "products/about.html")


def clothing(request): 
    """
    Dresses Page.
    """
    is_admin: bool = request.user.is_superuser
    items = Product.objects.filter(top_category__name='clothing').order_by('-created_at')
    items = [item.check_availabality() for item in items]

    items_per_page = 12
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page, 'is_admin': is_admin}
    return render(request, "products/clothing.html", context)


def garniture(request): 
    """
    Blankets Page.
    """
    is_admin: bool = request.user.is_superuser
    items = Product.objects.filter(top_category__name='garniture').order_by('-created_at')
    items = [item.check_availabality() for item in items]

    items_per_page = 12
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page, 'is_admin': is_admin}
    return render(request, "products/garniture.html", context)


def jackets(request): 
    """
    Blankets Page.
    """
    is_admin: bool = request.is_superuser
    items = Product.objects.filter(category__name='jacket').order_by('-created_at')
    items = [item.check_availabality() for item in items]
    items_per_page = 12
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page, 'is_admin': is_admin}
    return render(request, "products/jackets.html", context)


def newsletter(request):
    """
    News Letter Page - For vistors keen to be notified about novelties.
    """
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            follower = Follower.objects.create(
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                category=form.cleaned_data['category']
            )
            follower.save()
            return redirect('products:index')
        else:
            print("Invalid form submission. Data:", request.POST)
    else:
        form = NewsLetterForm()
    context = {'form': form}
    return render(request, "products/newsletter.html", context)
    

def search(request):
    """
    Getting the search query written in the searchbar and 
    passing it and redirecting to the search results view.
    """
    if request.method == 'GET':
        query = request.GET.get('q')
        return redirect('products:search-results', query=query)
    return HttpResponseBadRequest("Bad Request")


def search_results(request, query):
    """
    Rendering the search results queried by the user.
    """
    items = Product.objects.filter(
        Q(name__icontains=query) |
        Q(top_category__name__icontains=query) |
        Q(mid_category__name__icontains=query) |
        Q(bottom_category__name__icontains=query)
    ).order_by('-created_at')

    items_per_page = 4
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')

    items = paginator.get_page(page_number)

    context = {
        'searched': query,
        'items': items,
    }
    return render(request, 'products/search.html', context)

    

def item(request, product_pk):
    """
    Item/Product view.
    """
    item = Product.objects.get(pk=product_pk)
    images = None
    item_images = item.images
    if item_images.exists():
        images = item.images.all()
    context = {'item': item, 'images': images}
    return render(request, "products/item.html", context)


def mid_category_products(request, mid_category_pk):
    """
    Shows a specific mid category products.
    """
    # check if the category has a sub-category
    # if MidCategory.objects.filter(bottom_category__is_null=False):
    items = Product.objects.filter(mid_category_id=mid_category_pk)
    bottom_categories = BottomCategory.objects.filter(mid_category_id=mid_category_pk)
    mid_category = MidCategory.objects.get(pk=mid_category_pk)
    top_category = mid_category.top_category
    results_no = items.count()
    items_per_page = 12
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page, 
        'results_no': results_no,
        'top_category': top_category,  
        'mid_category': mid_category,
        'bottom_categories': bottom_categories
    }
    return render(request, "products/category.html", context)


def location(request):
    """
    
    """
    context = {'': ''}
    return render(request, "products/location.html", context)