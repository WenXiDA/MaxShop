from datetime import datetime


from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField

# Create your models here.


class GoodsCategory(models.Model):
    '''
    商品类别
    '''
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    des = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True,  blank=True, verbose_name="父类别", related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    '''
    品牌名
    '''
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    des = models.TextField(default="", verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(upload_to="brands/", verbose_name="品牌LOG", help_text="品牌LOG")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    '''
    商品
    '''
    category = models.ForeignKey(to=GoodsCategory, null=True, blank=True, verbose_name="商品类目", on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(default="", max_length=300, verbose_name="商品名", help_text="商品名")
    click_num = models.IntegerField(default=0, verbose_name="点击量", help_text="点击量")
    sold_num = models.IntegerField(default=0, verbose_name="销售量", help_text="销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏量", help_text="收藏量")
    goods_num = models.IntegerField(default=0, verbose_name="库存量", help_text="库存量")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.TextField(default="", verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=1000, filePath="goods/files/", default="")
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    goods_font_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='category',verbose_name="商品类目", on_delete=models.CASCADE)
    goods =models.ForeignKey(Goods, related_name='goods', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '首页商品类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(models.Model):
    '''
    商品轮播图
    '''
    goods = models.ForeignKey(to=Goods, verbose_name="商品", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="图片")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    '''
    轮播的商品
    '''
    goods = models.ForeignKey(to=Goods, verbose_name="商品", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", null=True, blank=True, verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name