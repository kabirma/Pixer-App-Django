from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def blogCategories(request,search):
    blogCategories= BlogCategory.objects.filter(name__icontains=search)
    serializer = BlogCategorySerializer(blogCategories,many=True)
    return Response({'status':200,'message':"Data Exist","data":serializer.data})

@api_view(['GET'])
def blogs(request):
    blogs= Blog.objects.all()
    serializer = BlogSerializer(blogs,many=True)
    return Response({'status':200,'message':"Data Exist","data":serializer.data})
