from django import forms
from .models import Ticket
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


class LoginForm(AuthenticationForm):
    pass
