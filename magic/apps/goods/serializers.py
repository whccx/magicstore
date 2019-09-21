from rest_framework import serializers
from goods.models import GoodsBase,Type,Order


# 业务逻辑(单字段），优先级：1
# def ccxname(data):
#     if data == 1234:
#         print('haha')
#     else:
#         print("nono")


class GoodsSerializer(serializers.ModelSerializer):
    #type_num = TypeSerializer()
    #type_num = serializers.IntegerField(source="type_num.num")
    #ccx = serializers.IntegerField(write_only=True,validators=[ccxname])

    #业务逻辑(单字段），优先级：2
    # def validate_ccx(self, data):
    #     if data == 1234:
    #         print('hi')
    #     else:
    #         print("no")

    #验证(attrs:POST数据)，优先级：3
    # def validate(self, attrs):
    #     # 删除自定义字段(创建和更新）
    #     del attrs["ccx"]
    #     return attrs

    class Meta:
        model = GoodsBase
        fields = '__all__'

        #性设置为从序列化中排除的字段列表
        # exclude = ('fjdskfjk',)

        #使用 depth 自关联外键ForeignKey
        depth = 1


class TypeSerializer(serializers.ModelSerializer):
    #一对多
    #type_num = GoodsSerializer(many=True)
    class Meta:
        model = Type
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'