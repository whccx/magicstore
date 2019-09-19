from django.contrib import admin
from goods.models import GoodsBase,Type

# Register your models here.
admin.site.register(GoodsBase)
admin.site.register(Type)