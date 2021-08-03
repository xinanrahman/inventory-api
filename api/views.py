from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter
from rest_framework import status 
from . import serializers
from . import models 

# Create your views here.
# class ItemAPIView(APIView):
#     def get(self, request):
#         items = models.Item.objects.all()
#         serializer = serializers.ItemSerializer(items, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = serializers.ItemSerializer(data=request.data)
#         print(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "message": "item saved successfully"
#             })

#         return Response(serializer.errors)

class ItemAPIView(ListCreateAPIView):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']