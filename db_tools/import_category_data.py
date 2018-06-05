import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MaxShop.settings")

import django
django.setup()

from goods.models import GoodsCategory

from db_tools.data.category_data import row_data


def add_cate(parent_cate, parent_cate_instance, deap):
    cates = parent_cate.get("sub_categorys", None)
    if cates:
        for sub_cate in cates:
            cate_instance = GoodsCategory()
            cate_instance.name = sub_cate["name"]
            cate_instance.code = sub_cate["code"]
            cate_instance.parent_category = parent_cate_instance
            cate_instance.category_type = deap+1
            cate_instance.save()
            add_cate(sub_cate, cate_instance, deap+1)
    else:
        return


for cate in row_data:
    cate_instance = GoodsCategory()
    cate_instance.name = cate["name"]
    cate_instance.code = cate["code"]
    cate_instance.category_type = 1
    cate_instance.save()
    add_cate(cate, cate_instance, deap=1)
