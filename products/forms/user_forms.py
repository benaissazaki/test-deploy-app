from django import forms
from ..models import Follower, TopCategory, MidCategory, BottomCategory
from django.core.exceptions import ValidationError


class NewsLetterForm(forms.ModelForm): 
    email = forms.EmailField(
        min_length=8, 
        max_length=30, 
        required=True,         
        widget=forms.TextInput(
            attrs={
                'id': 'customer-email',
                'class': 'newsletter-field', 
                'placeholder': 'Adresse Email',
            }
        ),
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'id': 'customer-phone',
                'class': 'newsletter-field', 
                'placeholder': 'Numero de telephone',
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset=MidCategory.objects.all(), 
        required=False,
        widget=forms.Select(
            attrs={
                'id': 'customer-category',
                'class': 'newsletter-field',
                'placeholder': 'Produit(s)',
            }
        )
    )

    class Meta:
        model  = Follower
        fields = ("email", "phone", "category")

    def clean_category(self):
        category = self.cleaned_data['category']
        if '-' in category and self.has_no_letters(category):
            raise ValidationError('This field is required.')
        return category
    
    @staticmethod
    def has_no_letters(word: str) -> bool:
        return not any(char.isalpha() for char in word)

