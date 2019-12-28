from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls import url
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'List_customers', views.CustomerView)
router.register(r'List_addresses', views.AddressView)
router.register(r'List_orders', views.OrderView)
router.register(r'List_products', views.ProductView)

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^customer/add/$', views.CustomerCreate.as_view(), name = 'customer-add'),
    url(r'^customer/(?P<pk>[0-9]+)/$', views.CustomerUpdate.as_view(), name = 'customer-update'),
    url(r'^customer/(?P<pk>[0-9]+)/delete/$', views.CustomerDelete.as_view(), name = 'customer-delete'),
    url(r'^address/add/$', views.AddressCreate.as_view(), name = 'address-add'),
    url(r'^address/(?P<pk>[0-9]+)/$', views.AddressUpdate.as_view(), name = 'address-update'),
    url(r'^address/(?P<pk>[0-9]+)/delete/$', views.AddressDelete.as_view(), name = 'address-delete'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
