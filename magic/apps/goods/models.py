from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


#相应上传图片-名字/路径
from django.urls import reverse
from uuid import uuid4

def goods_main(instance, filename):
	upload_to = 'goods_main'
	ext = filename.split('.')[-1]
	filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def goods_type(instance, filename):
	upload_to = 'goods_type'
	ext = filename.split('.')[-1]
	filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

#=============================================================
#商品基础信息表
class GoodsBase(models.Model):
	#快递设置
	express_choices = (('baoyou','卖家包邮'),('daofu','买家到付'),)

	name = models.CharField(max_length=50,verbose_name='商品名称')
	goods_num = models.CharField(max_length=50,verbose_name='商品编号')
	main_img = models.ImageField(upload_to=goods_main,verbose_name='商品主图',blank=True,null=True)
	#默认不限购
	limit_num = models.IntegerField(verbose_name='限购数量',default=0)
	out_stock = models.IntegerField(verbose_name='上架数量')
	upper = models.DateTimeField(default=datetime.now,verbose_name='上架时间')
	lower = models.CharField(max_length=20,verbose_name='下架时间',blank=True,default='')
	all_stock = models.IntegerField(verbose_name='仓库库存')
	ratio = models.IntegerField(verbose_name='打几折')
	sale_price = models.DecimalField(max_digits=20,decimal_places=2,verbose_name='市场价')
	cost_price = models.DecimalField(max_digits=20,decimal_places=2,verbose_name='成本价')
	start_time = models.CharField(max_length=20,verbose_name='开卖时间',blank=True,default='')
	allimg = UEditorField(
        verbose_name='商品详情',
        height=400,width=700,
        imagePath="arts/",filePath='file/',
        toolbars='full',command=None,
        upload_settings={"imageMaxSize": 2048000},
        settings={},default=u'',
    )
	express = models.CharField(choices=express_choices,max_length=10,verbose_name='快递方式')
	type_num = models.ForeignKey('Type',on_delete=models.CASCADE,related_name='type_num',verbose_name='分类编码')

	def __str__(self):
		return self.goods_num

	class Meta:
		verbose_name = '基础信息'
		verbose_name_plural = '基础信息'


#商品分类表
#========================================
class Type(models.Model):
	num = models.IntegerField(verbose_name='分类编号')
	name = models.CharField(max_length=20,verbose_name='分类名称')
	f_num = models.IntegerField(verbose_name='父类编号',default=0)
	ico = models.ImageField(upload_to=goods_type,verbose_name='子类图标',blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '商品分类'
		verbose_name_plural = '商品分类'

#=============================================================
#订单信息表
class Order(models.Model):
	#状态\进度选择
	state_choices = (
		('not_pay','未付款'),
		('ok_pay','已付款'),
		('send_goods','已发货'),
		('get_goods','确认收货'),
		('success','交易成功'),
		('cancel','已撤销'),
	)

	order_num = models.CharField(max_length=50,verbose_name='订单编号')
	buy_phone = models.CharField(max_length=20,verbose_name='买家')
	goods_num = models.CharField(max_length=50,verbose_name='商品编号')
	buy_num = models.IntegerField(verbose_name='购买数量')
	pay_money = models.DecimalField(max_digits=20,decimal_places=2,verbose_name='订单总价格')
	buy_time = models.DateTimeField(default=datetime.now,verbose_name='购买时间')
	state = models.CharField(max_length=20,choices=state_choices,verbose_name='进度状态',default='cancel')
	finish_time = models.CharField(max_length=20,verbose_name='完成时间',blank=True)
	buy_addr = models.CharField(max_length=50,verbose_name='收货地址',blank=True)

	def __str__(self):
		return self.order_num

	class Meta:
		verbose_name = '订单信息'
		verbose_name_plural = '订单信息'