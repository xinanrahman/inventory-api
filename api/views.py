from django.db.models import query
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.filters import SearchFilter
from . import pagination
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
    pagination_class = pagination.ItemPagination
    queryset = models.Item.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']


# class ItemDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = serializers.ItemSerializer
#     queryset = models.Item.objects.all()

class ItemDetailView(APIView):
    # def get_object(self, pk):
    #     item = get_object_or_404(models.Item, pk=pk)
    #     return item 

    def get(self, request, pk):
        item = get_object_or_404(models.Item, pk=pk)
        serializer = serializers.ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = get_object_or_404(models.Item, pk=pk)
        serializer = serializers.ItemSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        item = get_object_or_404(models.Item, pk=pk)
        item.delete()
        return Response({
            "alert": "item deleted..."
        })

    

