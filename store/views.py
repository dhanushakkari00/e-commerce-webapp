from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Collection,Review,Cart
from rest_framework import status
from .serializers import ProductSerializer,CollectionSerializer,ReviewSerializer,CartSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.viewsets import ModelViewSet,GenericViewSet

class ProductViewSet(ModelViewSet):
   queryset = Product.objects.select_related('collection').all()
   serializer_class = ProductSerializer

   def get_serializer_context(self):
    return {'request':self.request}
    
   def delete(self,request,id):
    product = get_object_or_404(Product, pk = id)
    if product.orderitems.count() >0:
        return Response({'error':'Product cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    def delete(self,request,id):
        collection = get_object_or_404(Collection , pk = id)
        if collection.product.count() >0:
            return Response({'error':'Collection cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # def get(self, request):
    #     queryset = Product.objects.select_related('collection').all()
    #     serializer = ProductSerializer(queryset,many = True, context = {'request':request})
    #     return Response(serializer.data)
    # def post(self, request):
    #     serializer = ProductSerializer(data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.validated_data
    #     serializer.save()
    #     return Response(serializer.data, status= status.HTTP_201_CREATED)

    lookup_field = 'id'
    # def get(self, request,id):
    #     product = get_object_or_404(Product, pk = id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # def put(self,request,id):
    #     product = get_object_or_404(Product, pk = id)
    #     serializer = ProductSerializer(product,data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

# @api_view(['GET','POST','DELETE'])
# def product_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(queryset,many = True, context = {'request':request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.validated_data
#         serializer.save()
#         return Response(serializer.data, status= status.HTTP_201_CREATED)

# @api_view(['GET','PUT','PATCH','DELETE'])
# def product_detail(request,id):

#     product = get_object_or_404(Product, pk = id)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product,data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method =='DELETE':
#         if product.orderitems.count() >0:
#             return Response({'error':'Product cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','PATCH','DELETE'])
def collection_detail(request,id):
    collection = get_object_or_404(Collection , pk = id)
    if request.method =='GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method=='DELETE':
        if collection.product.count() >0:
            return Response({'error':'Collection cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.all()
        serializer = CollectionSerializer(queryset,many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer = CollectionSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class ReviewModelSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CartViewSet(CreateModelMixin,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
