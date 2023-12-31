from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('', views.index, name='index'),
    path('provider/', views.list_provider, name='provider_list'),
    path('leader/', views.list_elder, name='elder_list'),
    path('ticket/detail/<str:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
    path('ticket/detail/edit/<str:ticket_id>', views.edit_ticket, name='edit_ticket'),
    path('ticket/detail/delete/<str:ticket_id>', views.delete_ticket, name='delete_ticket'),
    path('ticket/detail/<int:ticket_id>/comment/', views.add_comment, name='add_comment'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('add_provider/', views.add_provider, name='add_provider'),
    path('add_elder/', views.add_elder, name='add_elder'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
