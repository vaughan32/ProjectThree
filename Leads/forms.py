from django  import forms
from Leads.models import UserLead,UserAgent

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = UserLead
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
            'description',
            'agent_lead',
            'phone_number'
        ]

class AssignLeadForm(forms.Form):
    assign_agent = forms.ModelChoiceField(queryset=UserAgent.objects.none())

    def __init__(self,*args,**kwargs):
        request = kwargs.pop('request')
        agents = UserAgent.objects.filter(profile_agent = request.user.userprofile)
        super(AssignLeadForm,self).__init__(*args,**kwargs)
        self.fields['assign_agent'].queryset = agents