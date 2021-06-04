from django.contrib import admin

# Register your models here.

#user defined code
from .models import *

admin.site.register(cpeoples)
admin.site.register(capinitials)
admin.site.register(userbox)
admin.site.register(user_work)

