from rest_framework import serializers
from goods.models import GoodsBase

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBase
        fields = "__all__"

class AdminGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBase
        fields = "__all__"