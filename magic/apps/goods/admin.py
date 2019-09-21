from django.contrib import admin
from goods.models import GoodsBase,Type,Order

# Register your models here.
admin.site.register(GoodsBase)
admin.site.register(Type)
admin.site.register(Order)