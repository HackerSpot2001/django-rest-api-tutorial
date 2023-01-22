from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
# # Create your views here.

@csrf_exempt
@swagger_auto_schema(methods=['GET','POST'])
@api_view(['POST','GET'])
def index(req):
    if req.method == "GET":
        data = Product.objects.order_by('-date_created').all()
        data = ProductSerializer(data,many=True)
        return JsonResponse(data.data,safe=False)
    
    if req.method == "POST":
        data = JSONParser().parse(req)
        serial = ProductSerializer(data=data)
        if serial.is_valid():
            serial.save()

        return JsonResponse(serial.data, status=201)


# This will handle all operations
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    