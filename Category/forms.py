from django  import forms
from Leads.models import UserLead,UserCategory

class LeadCategoryForm(forms.ModelForm):
    class Meta:
        model = UserLead
        fields = ['category_lead']

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = UserCategory
        fields = ['category_name']
