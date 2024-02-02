from django.http import JsonResponse
from django.db.models import Q

from ..models import Product, Follower
from ..utils import is_valid_email


def newsletter(request):
    """
    This endpoint receives data from the client to create a new db entry and returns 
    a Json response to reflect the success or the failure of the operation. 
    """
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    confirm_email = request.GET.get('confirm_email')
    choice = request.GET.get('choice')

    if not first_name.isalpha():
        return JsonResponse({'response': 'invalid-first-name'})
    if not last_name.isalpha():
        return JsonResponse({'response': 'invalid-last-name'})
    if not is_valid_email(email):
        return JsonResponse({'response': 'invalid-email'})
    if not email == confirm_email:
        return JsonResponse({'response': 'unmatching-email'})
    if Follower.objects.filter(email=email).exists():
        return JsonResponse({'response': 'existing-email'})
    
    _, new_follower = Follower.objects.get_or_create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        category=choice
    )
    if new_follower:
        response = 'success'
    else:
        response = 'failure'
    return JsonResponse({'response': response})


def search_autocomplete(request):
    """
    Search Auto Complete, suggests items based on Products and Categories.
    """
    items = None
    if 'term' in request.GET:
        query = request.GET.get('term')
        search_results = Product.objects.filter(
            Q(name__icontains=query) |
            Q(mid_category__name__icontains=query)
        ).order_by('-created_at')[:5]
        if search_results.exists():
            items = [
                (
                    item.image.url, 
                    item.name, 
                    item.price, 
                    item.mid_category.name, 
                    item.pk
                ) for item in search_results
            ]
    return JsonResponse({'items': items, 'searched': query}, safe=False)



