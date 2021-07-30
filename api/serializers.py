from rest_framework import serializers
from . import models 


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item 
        fields = ("title", "price", "in_stock")