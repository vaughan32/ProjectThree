from django.views import generic
from Leads.models import UserLead,UserCategory
from django.urls import reverse
from Leads.forms import LeadModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from Agents.mixins import OrgarnizerCheckLoginRequiredMixin
from Leads.forms import AssignLeadForm

class LandingPage(generic.TemplateView):
    template_name = 'Leads/landing_page.html'

class LeadList(LoginRequiredMixin,generic.ListView):
    context_object_name = 'all_leads'
    
    template_name = 'Leads/lead_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserLead.objects.filter(profile_lead = user.userprofile,agent_lead__isnull = False)
        else:
            queryset = UserLead.objects.filter(profile_lead = user.useragent.profile_agent,agent_lead__isnull = False)
            queryset = queryset.filter(agent_lead__user_agent = user)
        return queryset

    def get_context_data(self, **kwargs):
        context =  super(LeadList,self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserLead.objects.filter(profile_lead = user.userprofile,agent_lead__isnull = True)
            context.update({
            'unassigned_leads' : queryset
           
             })
        return context

class LeadDetails(LoginRequiredMixin,generic.DetailView):
    context_object_name = 'lead_detail'
    template_name = 'Leads/lead_detail.html'
    def get_queryset(self):
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserLead.objects.filter(profile_lead = user.userprofile)
        else:
            queryset = UserLead.objects.filter(profile_lead = user.useragent.profile_agent)
            queryset = queryset.filter(agent_lead__user_agent = user)
        return queryset

class LeadCreate(OrgarnizerCheckLoginRequiredMixin,generic.CreateView):
    template_name = 'Leads/lead_create.html' 
    form_class = LeadModelForm

    def form_valid(self, form):
        profile_lead = form.save(commit=False)
        profile_lead.profile_lead = self.request.user.userprofile
        profile_lead.save()
        return super(LeadCreate,self).form_valid(form)

    def get_success_url(self):
        return reverse('lead_list')

class LeadUpdate(OrgarnizerCheckLoginRequiredMixin,generic.UpdateView):
    context_object_name = 'lead_detail'
    template_name = 'Leads/lead_update.html'
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserLead.objects.filter(profile_lead = user.userprofile)
        return queryset

    def get_success_url(self):
        return reverse('lead_list')

class LeadDelete(OrgarnizerCheckLoginRequiredMixin,generic.DeleteView):
    template_name = 'Leads/lead_delete.html'
    context_object_name = 'lead_detail'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserLead.objects.filter(profile_lead = user.userprofile)
        return queryset

    def get_success_url(self):
        return reverse('lead_list')

class AssignLeadToAgent(OrgarnizerCheckLoginRequiredMixin,generic.FormView):
    template_name = 'Leads/assign_leads.html'
    form_class = AssignLeadForm
    context_object_name = 'lead_detail'

    def get_form_kwargs(self,**kwargs):
        kwargs = super(AssignLeadToAgent,self).get_form_kwargs(**kwargs)
        kwargs.update({'request' : self.request})
        return kwargs

    def form_valid(self,form):
        collected_agent = form.cleaned_data['assign_agent']
        assign_to_lead = UserLead.objects.get(id = self.kwargs['pk'])
        assign_to_lead.agent_lead = collected_agent
        assign_to_lead.save()
        return super(AssignLeadToAgent,self).form_valid(form)

    def get_success_url(self):
        return reverse('lead_list')
