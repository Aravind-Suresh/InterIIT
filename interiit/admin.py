from django.contrib import admin
from interiit.models import Profile, Details

class DetailsAdmin(admin.ModelAdmin):
	list_display = ('pk', 'user', 'sport', 'college')
admin.site.register(Details, DetailsAdmin)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('pk', 'first_name', 'middle_name', 'last_name', 'phone_number', 'email_id', 'date_of_birth', 'timestamp')
admin.site.register(Profile, ProfileAdmin)
