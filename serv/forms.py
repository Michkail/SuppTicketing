from django import forms
from .models import Ticket, ContactRelation, ContactLeader
from django.contrib.auth.forms import AuthenticationForm


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'media', 'categories', 'location', 'assignee', 'status', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'assignee': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'media': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }


class ProviderForm(forms.ModelForm):
    class Meta:
        model = ContactRelation
        fields = ['provider', 'contact', 'address', 'maps', 'id_customer']
        widgets = {
            'provider': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'maps': forms.URLInput(attrs={'class': 'form-control'}),
            'id_customer': forms.TextInput(attrs={'class': 'form-control'})
        }


class LeaderForm(forms.ModelForm):
    class Meta:
        model = ContactLeader
        fields = ['name', 'contact', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'})
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input'}))
