import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MaxShop.settings")

import django
django.setup()

from db_tools.data.product_data import row_data
from goods.models import Goods, GoodsCategory, GoodsImage


for data in row_data:
    goods = Goods()
    goods.name = data["name"]
    goods.shop_price = float(int(data["sale_price"].replace("￥", "").replace("元", "")))
    goods.market_price = float(int(data["market_price"].replace("￥", "").replace("元", "")))
    goods.goods_brief = data["desc"] if data["desc"] is not None else ""
    goods.goods_desc = data["goods_desc"] if data["goods_desc"] is not None else ""
    goods.goods_font_image = data["images"][0] if data["images"] else ""
    goodscategory = GoodsCategory.objects.filter(name=data["categorys"][-1])[0]
    if goodscategory:
        goods.category = goodscategory
    goods.save()

    for image in data["images"]:
        goods_image = GoodsImage()
        goods_image.image = image
        goods_image.goods = goods
        goods_image.save()