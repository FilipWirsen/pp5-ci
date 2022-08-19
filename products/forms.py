from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Review


class ProductForm(forms.ModelForm):
    """ Form to add and edit products """

    class Meta:
        model = Product
        exclude = ('discounted_price',)
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """ Form for reviewing products """

    class Meta:
        model = Review
        fields = ('user_rating',)
    
    def __init__(self, *args, **kwargs):
        """ Remove auto-generated label and add placeholder and classes """
        super().__init__(*args, **kwargs)
        self.fields['user_rating'].widget.attrs['autofocus'] = True
        self.fields['user_rating'].widget.attrs = {'min': 0, 'max': 5}
        self.fields['user_rating'].widget.attrs['class'] = 'rounded-0 border-black'
        self.fields['user_rating'].widget.attrs['placeholder'] = '0-5 *'