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
    path('ticket/<str:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('add_provider/', views.add_provider, name='add_provider'),
    path('add_elder/', views.add_elder, name='add_elder'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
