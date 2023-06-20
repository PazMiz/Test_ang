from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(req):
    return Response("hello")


@api_view(['POST'])
def register(request):
        user = User.objects.create_user(username= request.data["username"],password=request.data['password'],is_staff=1,is_superuser=1)
        return Response({"reg":"User Register"})


@api_view(['GET'])
def about(req):
    return Response('about')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_only_view(request):
    if not request.user.is_staff:
        return Response("You are not authorized to access this view.", status=403)
    
    return Response("This is an admin-only view and only paz can reach it.")



@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response("This is a public view evrey employe on paz company can reach this.")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class products_view(APIView):
    def get(self, request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):
        # usr =request.user
        serializer = ProductSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



