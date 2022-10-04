from django.contrib import admin
from Leads.models import User,UserAgent,UserLead,UserProfile,UserCategory
admin.site.register(UserLead)
admin.site.register(UserAgent)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserCategory)