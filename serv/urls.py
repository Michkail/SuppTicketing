from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<int:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
    path('add_ticket/', views.add_ticket, name='add_ticket')
]
