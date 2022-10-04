from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from Authentications.forms import UserForm

class RegisterView(generic.CreateView):
    template_name = 'Leads/lead_create.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('login')