from django.urls import path
from . import views

urlpatterns = [
    path('lead_list/',views.LeadList.as_view(),name='lead_list'),
    path('lead_detail/<int:pk>/',views.LeadDetails.as_view(),name='lead_detail'),
    path('lead_create/',views.LeadCreate.as_view(),name='lead_create'),
    path('lead_update/<int:pk>/',views.LeadUpdate.as_view(),name='lead_update'),
    path('lead_delete/<int:pk>/',views.LeadDelete.as_view(),name='lead_delete'),
    path('lead_assign/<int:pk>/',views.AssignLeadToAgent.as_view(),name='lead_assign_agent'),
   
]