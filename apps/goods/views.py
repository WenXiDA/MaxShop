from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins

from goods.serializers import GoodsSerializer,GoodsImageSerializer
from goods.models import Goods, GoodsImage

# Create your views here.


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer


class GoodsimageListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsImage.objects.all()
    serializer_class = GoodsImageSerializer