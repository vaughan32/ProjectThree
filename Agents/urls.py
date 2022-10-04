from django.urls import path
from . import views

urlpatterns = [
    path('agent_list/',views.AgentList.as_view(), name='agent_list'),
    path('agent_create/',views.AgentCreate.as_view(), name='agent_create'),
    path('agent_detail/<int:pk>/',views.AgentDetail.as_view(), name='agent_detail'),
    # path('agent_update/<int:pk>/',views.AgentUpdate.as_view(), name='agent_update'),
    path('agent_delete/<int:pk>/',views.AgentDelete.as_view(), name='agent_delete'),
]