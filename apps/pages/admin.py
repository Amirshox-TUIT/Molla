from django.contrib import admin
from apps.pages.models import ContactModel, AboutModel

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    list_filter = ['created_at', ]
    search_fields = ['subject', 'email']

@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'profession',]
    list_filter = ['created_at', ]
    search_fields = ['profession', 'full_name', ]


