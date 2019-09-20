from rest_framework import serializers
from goods.models import GoodsBase

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBase
        fields = "__all__"

        #性设置为从序列化中排除的字段列表
        #exclude = ('limit_num',)

        #使用 depth 自关联外键ForeignKey
        depth = 1