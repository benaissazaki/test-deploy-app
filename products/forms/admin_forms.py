from django import forms
from ..models import TopCategory, MidCategory, Product, ProductImage, Purchase, BottomCategory
from django.core.exceptions import ValidationError


class AdminProductUploadForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'product-name',
                'class': 'admin-upload', 
                'placeholder': 'Nom du produit',
            }
        ),
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'product-name',
                'class': 'admin-upload', 
                'placeholder': 'Description du produit',
            }
        )
    )
    image = forms.ImageField(
        required=True,
        label='Main image*',
        widget=forms.FileInput(
            attrs={
                'id': "product-image",
                'class': 'admin-upload', 
                'placeholder': 'Image', 
            }
        )
    )
    price = forms.FloatField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': "product-price",
                'class': 'admin-upload', 
                'placeholder': 'Prix',
            }
        )
    )
    stock = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': "product-stock",
                'class': 'admin-upload', 
                'placeholder': 'Nombre d\'article',
            }
        )
    )
    top_category = forms.ModelChoiceField(
        queryset=TopCategory.objects.all(), 
        required=True,
        label='Top Category*',
        widget=forms.Select(
            attrs={
                'id': "product-category",
                'class': 'admin-upload', 
                'placeholder': 'category',
            }
        )
    )    

    mid_category = forms.ModelChoiceField(
        queryset=MidCategory.objects.all(), 
        required=True,
        label='Mid Category*',
        widget=forms.Select(
            attrs={
                'id': "product-category",
                'class': 'admin-upload', 
                'placeholder': 'Category',
            }
        )
    )
    bottom_category = forms.ModelChoiceField(
        queryset=BottomCategory.objects.all(), 
        required=False,
        label='Bottom Category',
        widget=forms.Select(
            attrs={
                'id': "product-bottom-category",
                'class': 'admin-upload', 
                'placeholder': 'Bottom category',
            }
        )
    )

    class Meta:
        model  = Product
        fields = ('name', 'description', 'price', 'stock','top_category', 'mid_category', 'bottom_category', 'image')


class AdminUpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'stock', 'mid_category')


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, max_files=5, max_file_size=10 * 1024 * 1024, *args, **kwargs):
        self.max_files = max_files #TODO: Limits set doesn't seem to be working
        self.max_files_size = max_file_size
        kwargs.setdefault('widget', MultipleFileInput())
        super(MultipleFileField, self).__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        # field not required and no data provided
        single_file_clean = super(MultipleFileField, self).clean
        if isinstance(data, (list, tuple)):
            if len(data) > self.max_files:
                raise forms.ValidationError(f'You can upload up to {self.max_files} files only.')
            result = [single_file_clean(d, initial) for d in data]
            for file in result:
                if file.size > self.max_files_size:
                    raise forms.ValidationError(f'File size should not exceed {self.max_files_size} bytes.')
                else:
                    return result


class AdminProductImageForm(forms.Form):
    class Meta:
        model = ProductImage
        fields = ['extra_image']
    
    extra_image = MultipleFileField(
            required=False, 
            label='Extra images:',
            widget=MultipleFileInput(
                attrs={
                    'id': 'multiple-images',
                    'class': 'admin-upload',
                    'placeholder': 'Product extra images'
                }
            ),
        ) 


class AdminTopCategoryCreationForm(forms.ModelForm): 
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'top-category-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre category',
            }
        ),
    )
    confirm_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'top-category-confirm-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre category',
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'top-category-description',
                'class': 'admin-category', 
                'placeholder': 'Description de votre category',
            }
        )
    )

    def clean_confirm_name(self):
        """
        Confirm the category name given by 
        the admin is correct to avoid typos.
        """
        name = self.cleaned_data["name"]
        confirm_name = self.cleaned_data['confirm_name']
        if name != confirm_name:
            raise ValidationError("Category name doesn't match.")
        return name

    class Meta:
        model = TopCategory
        fields = ('name', 'confirm_name', 'description', 'image')



class AdminMidCategoryCreationForm(forms.ModelForm): 
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'category-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre category',
            }
        ),
    )
    confirm_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'category-confirm-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre category',
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'category-description',
                'class': 'admin-category', 
                'placeholder': 'Description de votre category',
            }
        )
    )
    top_category = forms.ModelChoiceField(
        queryset=TopCategory.objects.all(), 
        required=True,
        widget=forms.Select(
            attrs={
                'id': "top-category-choice",
                'class': 'admin-category', 
                'placeholder': 'category',
            }
        )
    )    

    def clean_confirm_name(self):
        """
        Confirm the category name given by 
        the admin is correct to avoid typos.
        """
        name = self.cleaned_data["name"]
        confirm_name = self.cleaned_data['confirm_name']
        if name != confirm_name:
            raise ValidationError("Category name doesn't match.")
        return name

    class Meta:
        model = MidCategory
        fields = ('name', 'confirm_name', 'description', 'top_category', 'image')


class AdminEditMidCategoryForm(forms.ModelForm):
    class Meta:
        model = MidCategory
        fields = ('name', 'image', 'description')


class AdminBottomCategoryCreationForm(forms.ModelForm): 
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'subcategory-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre sous category',
            }
        ),
    )
    confirm_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'subcategory-confirm-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre sous category',
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'subcategory-description',
                'class': 'admin-category', 
                'placeholder': 'Description de votre sous category',
            }
        )
    )
    mid_category = forms.ModelChoiceField(
        queryset=MidCategory.objects.all(), 
        required=True,
        widget=forms.Select(
            attrs={
                'id': "subcategory-category",
                'class': 'admin-category', 
                'placeholder': 'category',
            }
        )
    )

    def clean_confirm_name(self):
        """
        Confirm the category name given by 
        the admin is correct to avoid typos.
        """
        name = self.cleaned_data["name"]
        confirm_name = self.cleaned_data['confirm_name']
        if name != confirm_name:
            raise ValidationError("Category name doesn't match.")
        return name

    class Meta:
        model = BottomCategory
        fields = ('name', 'confirm_name', 'description', 'mid_category', 'image')


class AdminSaleConfirmationForm(forms.Form):
    quantity = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': "sale-quantity",
                'class': 'admin-sale-confirmation', 
                'placeholder': 'Nombre d\'articles vendus',
            }
        )
    )

    class Meta:
        model  = Purchase
        fields = ('quantity')



