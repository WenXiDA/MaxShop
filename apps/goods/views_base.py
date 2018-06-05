from rest_framework.response import Response
from rest_framework.views import APIView

from goods.serializers import GoodsSerializer
from goods.models import Goods

class GoodsListView(APIView):

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        rps = Response(goods_serializer.data)
        return rps