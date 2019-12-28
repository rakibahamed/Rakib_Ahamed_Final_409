from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from .serializers import *

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class OrderView(viewsets.ModelViewSet):
    queryset =Order.objects.all()
    serializer_class = OrderSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'customer_list'

    def get_queryset(self):
        return Customer.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = Customer.objects.all()
        context['address'] = Address.objects.all()
        context['order'] = Order.objects.all()
        context['product'] = Product.objects.all()
        return context

#class CustomerDetailView(generic.DetailView):
 #  model = Customer
  # template_name = 'customer.html'


class CustomerCreate(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'prime_customer']
    template_name = 'customer_form.html'
    success_url = reverse_lazy('index')


class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'prime_customer']
    template_name = 'customer_form.html'
    success_url = reverse_lazy('index')


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('index')


class AddressCreate(CreateView):
    model = Address
    fields = ['fk', 'street', 'city', 'state','zip']
    template_name = 'customer_form.html'
    success_url = reverse_lazy('index')


class AddressUpdate(UpdateView):
    model = Address
    fields = ['street', 'city', 'state','zip']
    template_name = 'customer_form.html'
    success_url = reverse_lazy('index')


class AddressDelete(DeleteView):
    model = Address
    success_url = reverse_lazy('index')

