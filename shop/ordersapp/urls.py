from django.urls import URLPattern, path
from . import views


app_name = 'ordersapp'
urlpatterns = [
    path('', views.OrderList.as_view(), name='orders-list'),
    path('create/', views.OrderCreate.as_view(), name='order-create'),
    path('detail/<int:pk>', views.OrderDetail.as_view(), name='order-detail'),
    path('update/<int:pk>', views.OrderUpdate.as_view(), name='order-update'),
    path('delete/<int:pk>', views.OrderDelete.as_view(), name='order-delete'),
    path(
        'forming/complete/<int:pk>',
        views.OrderList.as_view(),
        name='order-forming-complete'
        ),
]
