from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q

from ..models import Follower, Product, ProductImage, TopCategory, MidCategory, BottomCategory, Purchase

from ..forms.admin_forms import AdminProductUploadForm, AdminSaleConfirmationForm, AdminMidCategoryCreationForm, \
                                AdminBottomCategoryCreationForm, AdminEditMidCategoryForm, AdminUpdateProductForm, \
                                AdminTopCategoryCreationForm, AdminProductImageForm


def is_superuser(user):
    """
    Checking if the user is an admin for security purposes.
    """
    return user.is_superuser
    

@login_required
@user_passes_test(is_superuser)
def admin_upload_product(request):
    """
    Admin - Sending emails to the followers upon admin new content upload.
    """
    if request.method == 'POST':
        form = AdminProductUploadForm(request.POST, request.FILES)
        image_form = AdminProductUploadForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            product = form.save()
            images = request.FILES.getlist('extra_image')
            if images:
                for image in images:
                    product_image = ProductImage.objects.create(extra_image=image)
                    product_image.product.set([product]) 
            return redirect('products:dashboard')
        else:
            print(form.errors)
    else:
        form = AdminProductUploadForm()
        image_form = AdminProductImageForm()
        print(image_form.fields['extra_image'].required)
    context = {
                'form': form, 
                'image_form': image_form
            }
    return render(request, "admin/upload_content.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_product_sold(request, product_pk):
    """
    Admin - Confirm sale and update stock.
    """
    product = Product.objects.get(pk=product_pk)
    if request.method == 'POST':
        form = AdminSaleConfirmationForm(request.POST)
        if form.is_valid():
            Purchase.objects.create(
                quantity=form.cleaned_data['quantity'],
                product_id=product_pk
            )
            return redirect('products:dashboard')
    else:
        form = AdminSaleConfirmationForm()
    context = {'form': form, 'product': product}
    return render(request, "admin/confirm_sale.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_create_top_category(request):
    """
    Admin - Create a new unique category.
    """
    if request.method == 'POST':
        form = AdminTopCategoryCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:dashboard')
    else:
        form = AdminTopCategoryCreationForm()
    context = {'form': form}
    return render(request, "admin/create_top_category.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_create_mid_category(request):
    """
    Admin - Create a new unique category.
    """
    if request.method == 'POST':
        form = AdminMidCategoryCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:dashboard')
    else:
        form = AdminMidCategoryCreationForm()
    context = {'form': form}
    return render(request, "admin/create_category.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_create_bottom_category(request):
    """
    Admin - Create a new unique subcategory.
    """
    if request.method == 'POST':
        form = AdminBottomCategoryCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:dashboard')
    else:
        form = AdminBottomCategoryCreationForm()
    context = {'form': form}
    return render(request, "admin/create_subcategory.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_edit_category(request, category_pk):
    """
    Admin - Create a new unique category.
    """
    category = MidCategory.objects.get(pk=category_pk)
    if request.method == 'POST':
        form = AdminEditMidCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('products:dashboard')
    form = AdminEditMidCategoryForm(instance=category)
    context = {'form': form}
    return render(request, "admin/update_category.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_update_product(request, product_pk):
    """
    Admin - Create a new unique category.
    """
    product = Product.objects.get(pk=product_pk)
    if request.method == 'POST':
        form = AdminUpdateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:dashboard')
    form = AdminUpdateProductForm(instance=product)
    context = {'form': form}
    return render(request, "admin/update_product.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_full_purchases(request):
    """
    Admin - Purchases Page.
    """
    purchases = Purchase.objects.all()
    items_per_page = 12
    paginator = Paginator(purchases, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page}
    return render(request, "admin/full_purchases.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_full_purchase_details(request, product_pk):
    """
    Admin - Products' Full Purchase Details Page.
    """
    purchase = Purchase.objects.get(product_id=product_pk)
    context = {'purchase': purchase}
    return render(request, "admin/full_purchase_details.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_dashboard(request):
    """
    Admin - Dashboard view.
    """
    # purchase = Purchase.objects.get(product_id=product_pk)
    # context = {'purchase': purchase}
    return render(request, "admin/dashboard.html", context=None)


# no money tracking