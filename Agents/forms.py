from django import forms
from Leads.models import UserAgent
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateAnAgent(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']