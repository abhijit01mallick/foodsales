from asyncio.log import logger
from itertools import product
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from products.models import Foodsales

class productsview(APIView):
    def get(self, request, poll_id, format = "json"):
        try:
            #queryset = Foodsales.objects.filter(Product = str(request.GET.get("product"))).values()
            queryset = Foodsales.objects.filter(Product = poll_id).values()
            data = {"status": "success", "result" : queryset}
            return Response(data, status = status.HTTP_200_OK)
        except:
            logger.error('Some error occured')

class productsshow(APIView):
    def post(self, request, format = "json"):
        try:
            queryset = Foodsales.objects.filter(Product = request.data["product"]).values()[:5]
            #print(queryset)
            data = {"status": "success", "result" : queryset}
            return Response(data, status = status.HTTP_200_OK)
        except:
            logger.error('Some error occured')

    