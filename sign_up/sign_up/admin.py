from .models import signupModel
from django.contrib import admin
class signupAdmin(admin.ModelAdmin):
    list_display= ["sid","first_name","last_name","email_address","tech256_username"]
    class Meta:
        model = signupModel

admin.site.register(signupModel, signupAdmin)