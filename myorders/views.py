
# Rest-Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters import rest_framework as filters

from django.http import Http404

from rest_framework import status
from rest_framework.response import Response

# Project
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer, OrderItemSerializer
from .models import Customer, Product, Order, OrderItem


from .services import *


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



##########################################
class OrderItemList(APIView):
 
    def get(self, request, format=None):
        snippets = OrderItem.objects.all()
        serializer = OrderItemSerializer(snippets, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data.get('quantity')
        
            product = serializer.validated_data.get('product')

            serializer.validated_data['cost'] = quantity * product.cost

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#########################################3
class OrderItemAPIView(APIView):
    serializer_class = OrderItemSerializer

    def get_object(self, pk):
        try:
            return OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OrderItemSerializer(snippet)
        return Response(serializer.data)

    
    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = OrderItemSerializer(object, data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data.get('quantity')
            product = serializer.validated_data.get('product')

            serializer.validated_data['cost'] = quantity * product.cost

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class OrderList(APIView):
 
    def get(self, request, format=None):
        snippets = Order.objects.all()
        serializer = OrderSerializer(snippets, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
        
            order = serializer.save()

            total_sum = 0

            for item in order.products.all():
                total_sum+=item.cost

            order.summa = total_sum

            order.save()

            order.customer.dept = order.customer.dept + total_sum

            order.customer.save()

            

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderAPIView(APIView):
    serializer_class = OrderSerializer

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet)
        return Response(serializer.data)

    
    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = OrderSerializer(object, data=request.data)

        if serializer.is_valid():
            order = serializer.save()

            total_sum = 0

            for item in order.products.all():
                total_sum+=item.cost

            order.summa = total_sum
            
            order.save()

            order.customer.dept = order.customer.dept + total_sum

            order.customer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
# class OrderViewSet(ModelViewSet):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()


# class OrderItemViewSet(ModelViewSet):
#     serializer_class = OrderItemSerializer
#     queryset = OrderItem.objects.all()


# __all__ = ['CustomerViewSet', 'ProductViewSet', 'OrderViewSet', 'OrderItemViewSet']

__all__ = ['CustomerViewSet', 'ProductViewSet']



