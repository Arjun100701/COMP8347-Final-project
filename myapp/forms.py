# forms.py
from django import forms
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BuildingPermit, CustomUser, ContactModel


class AdminSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')


class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)


#User Signup
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

#User Login
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Required')


class BuildingPermitForm(forms.ModelForm):
    class Meta:
        model = BuildingPermit
        fields = ['name', 'contact_number', 'mail_id', 'city', 'province', 'area', 'floors', 'government_id_proof',
                  'land_purchase_record', 'user_id']

        widgets = {
            'area': forms.Select(choices=BuildingPermit.AREA_CHOICES),
            'floors': forms.Select(choices=BuildingPermit.FLOORS_CHOICES),
            'user_id': forms.HiddenInput(),
        }

    # Validation for Email and phone number
    def clean_mail_id(self):
        mail_id = self.cleaned_data['mail_id']
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', mail_id):
            raise ValidationError('Invalid email address')
        return mail_id

    def clean_contact_number(self):
        contact_number = self.cleaned_data['contact_number']
        if not re.match(r'^\+?1?\d{9,15}$', contact_number):
            raise ValidationError('Invalid contact number')
        return contact_number


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'id': 'form-p'})
        self.fields['email'].widget.attrs.update({'id': 'form-p'})
        self.fields['phone'].widget.attrs.update({'id': 'form-p'})
        self.fields['description'].widget.attrs.update({'id': 'form-p'})

    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'phone', 'description']


class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # This is to remove the ":" symbol from the end of the label
        kwargs.setdefault('label_suffix', '')
        super(SearchForm, self).__init__(*args, **kwargs)

    query = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'search-form',
                'placeholder': "Enter name, application status or application reference number to search...",
            }
        ),
        label='Search Applications',
    )
