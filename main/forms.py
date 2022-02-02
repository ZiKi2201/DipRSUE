from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from .models import Reviews
from .models import Applications


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['name_org', 'position', 'name', 'review', 'consent']

        widgets = {
            "name_org": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование вашей организации...'
            }),
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша должность...'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше полное имя...'
            }),
            "review": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш отзыв...'
            }),
            "consent": CheckboxInput(attrs={
                'class': 'checkbox-inline',
                'type': 'checkbox',
                'required': 'False',
                'initial': 'True'
            })
        }

class ApplicationsForm(ModelForm):
    class Meta:
        model = Applications
        fields = ['name', 'email', 'mobile', 'add_inf', 'consent']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя...'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'Ваш email...'
            }),
            "mobile": TextInput(attrs={
                'class': 'form-control',
                'type': 'tel',
                'placeholder': 'Ваш номер телефона...',
                'pattern': '^\+7\d{3}\d{7}$',
                'value': '+7',
                'maxlength': '12'
            }),
            "add_inf": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительная информация...',


            }),
            "consent": CheckboxInput(attrs={
                'class': 'checkbox-inline',
                'type': 'checkbox',
                'required': 'False',
                'initial': 'True'
            })
        }

        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data
