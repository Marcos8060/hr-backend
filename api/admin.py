from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Project)
admin.site.register(ApprovedProject)
admin.site.register(Leave)