"""View module for handling requests about types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hotelapi.models import Customer

class CustomerView(ViewSet):
  #GETS A SINGLE OBJECT FROM THE DB BASED ON THE PK IN THE URL
  #USE ORM TO GET DATA
  def retrieve(self, request, pk):
  #SERIALIZER CONVERTS DATA TO JSON  
    try:
      customer = Customer.objects.get(pk=pk)
      serializer = SingleCustomerSerializer(customer)
      return Response(serializer.data)
    except Customer.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    #GET ALL OJECTS FROM DATABASE. ORM IS ALL
    customers = Customer.objects.all()
    
    favorite = request.query_params.get('favorite', None)
    if favorite is not None:
      customers = customers.filter(favorite=favorite)
    
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)
  #POST REQUESTS
  def create(self, request):
    #VALUES FROM CLIENT/FIXTURES
    customer = Customer.objects.create(
      first_name=request.data["first_name"],
      last_name=request.data["last_name"],
    )
    serializer = CustomerSerializer(customer)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    
    id = pk
    customer = Customer.objects.get(pk=pk)
    customer.first_name = request.data["first_name"]
    customer.last_name = request.data["last_name"]
    
    customer.save()
    
    serializer = CustomerSerializer(customer)    
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  #SERIALIZER CLASS DETERMINES HOW PYTHON DATA SHOULD BE SERIALIZED TO BE SENT BACK TO CLIENT
class CustomerSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Customer
    fields = ('id','first_name', 'last_name')
    
class SingleCustomerSerializer(serializers.ModelSerializer):
  
 
  class Meta:
    model = Customer
    fields = ('id','first_name', 'last_name')
    depth = 1
