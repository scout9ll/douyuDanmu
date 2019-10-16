from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Lead
from .models import Room

# Register your models here.告诉对象需要被管理


admin.site.register(Lead)
admin.site.register(Room)
