from django.contrib import admin
from firstApp.models import AccessRecord, Topic, Webpage, UsersData
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UsersData)
