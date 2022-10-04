from django.views import generic
from Leads.models import UserCategory,UserLead
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from Agents.mixins import OrgarnizerCheckLoginRequiredMixin
from Category.forms import LeadCategoryForm,CreateCategoryForm


class CategoryListView(LoginRequiredMixin,generic.ListView):
    template_name = 'Category/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserCategory.objects.filter(category_profile = user.userprofile)
        else:
            queryset = UserCategory.objects.filter(category_profile = user.useragent.profile_agent)
        return queryset
 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserLead.objects.filter(profile_lead = user.userprofile)
        else:
            queryset = UserLead.objects.filter(profile_lead = user.useragent.profile_agent)
        context.update({
            'unassigned_leads_count' : queryset.filter(category_lead__isnull = True).count()
        })
        return context


class CategoryDetail(LoginRequiredMixin,generic.DetailView):
    template_name = 'Category/category_detail.html'
    context_object_name = 'category_detail'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserCategory.objects.filter(category_profile = user.userprofile)
        else:
            queryset = UserCategory.objects.filter(category_profile = user.useragent.profile_agent)
        return queryset

    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     category_lead = self.get_object().UserLead.all()
    #     context.update({'category_detail' : category_lead})
    #     return context
 
class CategoryUpdate(LoginRequiredMixin,generic.UpdateView):
    context_object_name = 'lead_detail'
    template_name = 'Category/category_update.html'
    form_class = LeadCategoryForm
    def get_queryset(self):
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserLead.objects.filter(profile_lead = user.userprofile)
        else:
            queryset = UserLead.objects.filter(profile_lead = user.useragent.profile_agent)
            queryset = queryset.filter(agent_lead__user_agent = user)
        return queryset
    
    def get_success_url(self):
        return reverse('category_update', kwargs={'pk' : self.get_object().id}) 

class CategoryCreate(OrgarnizerCheckLoginRequiredMixin,generic.CreateView):
    template_name = 'Category/category_create.html' 
    form_class = CreateCategoryForm
    
    def form_valid(self, form):
        category_orgarnization= form.save(commit=False)
        category_orgarnization.category_profile = self.request.user.userprofile
        category_orgarnization.save()
        return super(CategoryCreate,self).form_valid(form)

    def get_success_url(self):
        return reverse('category_list')


class CategoryFormUpdate(OrgarnizerCheckLoginRequiredMixin,generic.UpdateView):
    template_name = 'Category/category_updateform.html' 
    form_class = CreateCategoryForm
    context_object_name = 'category_updateform'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserCategory.objects.filter(category_profile = user.userprofile)
        else:
            queryset = UserCategory.objects.filter(category_profile = user.useragent.profile_agent)
        return queryset

    def get_success_url(self):
        return reverse('category_list')

class CategoryFormDelete(OrgarnizerCheckLoginRequiredMixin,generic.DeleteView):
    template_name = 'Category/category_delete.html'
    context_object_name = 'category_deleteform'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgarnizer:
            queryset = UserCategory.objects.filter(category_profile = user.userprofile)
        else:
            queryset = UserCategory.objects.filter(category_profile = user.useragent.profile_agent)
        return queryset

    def get_success_url(self):
        return reverse('category_list')