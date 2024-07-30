from django import forms
from .models import LibraryUser

class LibraryUserForm(forms.ModelForm):
    class Meta:
        model = LibraryUser
        fields = ['name', 'user_id', 'email']
