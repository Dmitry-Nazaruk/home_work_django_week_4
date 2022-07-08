from django.contrib import admin
from .models import Authors,Books,Profile,Member
# Register your models here.

admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Profile)
admin.site.register(Member)