from django import forms

from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'gsm', 'price', 'size',
                  'made_in', 'category', 'image', 'description']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Enter Product Name'
        self.fields['gsm'].widget.attrs['placeholder'] = 'Enter GSM'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter Price'
        self.fields['made_in'].widget.attrs['placeholder'] = 'Made In'
        self.fields['category'].widget.attrs['placeholder'] = 'Product Category'
        self.fields['description'].widget=forms.Textarea(attrs = {'class': 'form-control', 'placeholder': "Enter short description"})

