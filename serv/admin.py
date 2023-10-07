from django.contrib import admin
from .models import Ticket, ContactRelation, ContactLeader


class TicketAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	list_filter = ('status', 'assignee')
	list_display = ('id', 'title', 'status', 'assignee', 'description', 'location', 'updated_at')
	search_fields = ['title', 'status']


class ContactRelationPartner(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	list_filter = ('provider', 'contact')
	list_display = ('id', 'provider', 'contact', 'id_customer', 'updated_at')
	search_fields = ['provider']


class ContactLeaderAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	list_filter = ('name', 'contact')
	list_display = ('id', 'name', 'contact', 'location', 'updated_at')
	search_fields = ['name', 'location']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(ContactRelation, ContactRelationPartner)
admin.site.register(ContactLeader, ContactLeaderAdmin)
