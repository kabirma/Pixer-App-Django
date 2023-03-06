from rest_framework import serializers
from .models import *


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        # fields = ['id','name','created_at']
        # exclude = ['id']
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['description'] 

