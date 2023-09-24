from django import forms
from catalog.models import Product, Version

LIMITATIONS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'img', 'category', 'price']

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        for limitation in LIMITATIONS:
            if limitation in cleaned_name:
                raise forms.ValidationError('Ошибка, связанная с именем пользователя')

        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        for limitation in LIMITATIONS:
            if limitation in cleaned_description:
                raise forms.ValidationError('Ошибка, связанная с описанием')

        return cleaned_description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['number', 'name', 'active']
