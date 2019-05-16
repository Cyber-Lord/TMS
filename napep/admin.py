from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phoneNumber','first_name', 'last_name', 'contact_address']



admin.site.register(User, UserAdmin)
admin.site.register(Group)
admin.site.register(Tricycle)
admin.site.register(Rider)
admin.site.register(TricycleOwner)
admin.site.register(Brand)