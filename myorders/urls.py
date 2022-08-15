

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet, OrderItemList, OrderItemAPIView, OrderAPIView, OrderList

router = DefaultRouter()
router.register('customer', CustomerViewSet, 'customer')
router.register('product', ProductViewSet, 'product')
# router.register('order', OrderViewSet, 'order')
# router.register('order_item', OrderItemViewSet, 'order_item')


urlpatterns = [
    path('', include(router.urls)),
    path('order_item/', OrderItemList.as_view()),
    path('order_item/<int:pk>/', OrderItemAPIView.as_view()),
    path('order/', OrderList.as_view()),
    path('order/<int:pk>/', OrderAPIView.as_view()),

]



