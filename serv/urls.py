from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('', views.index, name='index'),
    path('ticket/<int:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
