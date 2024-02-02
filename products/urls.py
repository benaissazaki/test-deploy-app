from django.urls import path
from .views import user_views, admin_views, json_views

app_name = 'products'

urlpatterns = [
    # customer
    path('', user_views.index, name='index'),
    path('products-overview/', user_views.products, name='products'),
    path('about/', user_views.about, name='about'),
    path('clothing/', user_views.clothing, name='clothing'),
    path('garniture/', user_views.garniture, name='garniture'),
    path('location/', user_views.location, name='location'),
    path('news-letter/', user_views.newsletter, name='news-letter'),
    path('search/', user_views.search, name='search'),
    path('search-results/<query>/', user_views.search_results, name='search-results'),
    path('item/<product_pk>/', user_views.item, name='item'),
    path('category/<int:mid_category_pk>/', user_views.mid_category_products, name='category-products'),
    # admin
    path('upload-content/', admin_views.admin_upload_product, name='upload-content'),
    path('confirm-sale/<int:product_pk>/', admin_views.admin_product_sold, name='confirm-sale'),
    path('create-top-category/', admin_views.admin_create_top_category, name='create-top-category'),
    path('create-category/', admin_views.admin_create_mid_category, name='create-category'),
    path('create-subcategory/', admin_views.admin_create_bottom_category, name='create-subcategory'),
    path('edit-category/<int:category_pk>/', admin_views.admin_edit_category, name='edit-category'),
    path('update-product/<int:product_pk>/', admin_views.admin_update_product, name='update-product'),
    path('dashboard/', admin_views.admin_dashboard, name='dashboard'),
    # json
    path('newsletter/', json_views.newsletter, name='newsletter'),
    path('search-autocomplete/', json_views.search_autocomplete, name='search-autocomplete'),
]
 