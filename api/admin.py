from django.contrib import admin


from api.models import ClientUserInvite, Registration
# Register your models here.

admin.site.register(ClientUserInvite)
admin.site.register(Registration)
