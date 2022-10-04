import random
from django.views import generic
from django.core.mail import send_mail
from Leads.models import UserAgent
from django.urls import reverse
from Agents.forms import CreateAnAgent
from Agents.mixins import OrgarnizerCheckLoginRequiredMixin


class AgentList(OrgarnizerCheckLoginRequiredMixin,generic.ListView):
    template_name = 'Agents/agent_list.html'
    context_object_name = 'all_agents'
    
    def get_queryset(self):
        current_user = self.request.user
        user_profile = current_user.userprofile
        return UserAgent.objects.filter(profile_agent = user_profile)


class AgentCreate(OrgarnizerCheckLoginRequiredMixin,generic.CreateView):
    template_name = 'Agents/agent_create.html'
    form_class = CreateAnAgent

    def form_valid(self, form):
        agent_user = form.save(commit=False)
        agent_user.is_orgarnizer = False
        agent_user.is_agent = True
        agent_user.set_password(f'random.randint(0,1000000)')
        agent_user.save()
        UserAgent.objects.create(user_agent = agent_user,profile_agent = self.request.user.userprofile)
        send_mail(
            subject = 'You are Invited to be an agent',
            message = 'You were added as an agent on this app.kindly change your password, Login and start tasking',
            from_email= 'TheadminOfTheApp@gmail.com',
            recipient_list=[agent_user.email])
        return super(AgentCreate,self).form_valid(form)

    def get_success_url(self):
        return reverse('agent_list')


class AgentDetail(OrgarnizerCheckLoginRequiredMixin,generic.DetailView):
    template_name = 'Agents/agent_detail.html'
    context_object_name = 'agent_detail'

    def get_queryset(self):
        current_user = self.request.user
        user_profile = current_user.userprofile
        return UserAgent.objects.filter(profile_agent = user_profile)

class AgentUpdate(OrgarnizerCheckLoginRequiredMixin,generic.UpdateView):
    template_name = 'Agents/agent_update.html'
    form_class = CreateAnAgent
    context_object_name = 'agent_detail'

    def get_queryset(self):
        current_user = self.request.user
        user_profile = current_user.userprofile
        return UserAgent.objects.filter(profile_agent = user_profile)

    def get_success_url(self):
        return reverse('agent_list')

class AgentDelete(OrgarnizerCheckLoginRequiredMixin,generic.DeleteView):
    template_name = 'Agents/agent_delete.html'
    context_object_name = 'agent_detail'

    def get_queryset(self):
        current_user = self.request.user
        user_profile = current_user.userprofile
        return UserAgent.objects.filter(profile_agent = user_profile)

    def get_success_url(self):
        return reverse('agent_list')