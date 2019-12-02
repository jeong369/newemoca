from django.contrib import admin
from .models import Test, Score, Adjective

# Register your models here.
admin.site.register(Test)
admin.site.register(Score)
admin.site.register(Adjective)