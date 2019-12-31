from django.shortcuts import render
from .models import Good
from rest_framework import viewsets, filters, generics, views, status, pagination
from rest_framework.response import Response
from .serializer import GoodSerializer


# Create your views here.
class GoodsAPIViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all().order_by('-created_at')
    serializer_class = GoodSerializer

    def create(self, request, *args, **kwargs):
        print(request.POST)
        POST = request.POST.copy() #request.POST自体は書き換えられない仕様なのでコピー
        POST['name'] = POST['name'] + '!!'
        serializer = GoodSerializer(data=POST)
        serializer.is_valid(raise_exception=True)
        good = serializer.save()

        return Response({"detail":"accepted"}, status.HTTP_202_ACCEPTED)

class LatestGoodsAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        latest_goods = Good.objects.last()
        latest_goods = GoodSerializer(latest_goods)
        return Response({"latestGoods":latest_goods.data}, status.HTTP_200_OK)
