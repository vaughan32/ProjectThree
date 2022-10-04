from django.contrib import admin
from django.urls import path,include
from Leads.views import LandingPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPage.as_view(),name='landing_page'),
    path('leads/',include('Leads.urls')),
    path('authentications/',include('Authentications.urls')),
    path('category/',include('Category.urls')),
    path('agents/',include('Agents.urls'))
]
