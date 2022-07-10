from functools import partial
import io
from django.shortcuts import render
from .serializers import SerializerDetails,SerializerRecords
from .models import Dog,Breed
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


#ModelViewSet CRUD Operations

class DogModelViewSet(viewsets.ModelViewSet):
    queryset=Dog.objects.all()
    serializer_class=SerializerRecords
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class BreedModelViewSet(viewsets.ModelViewSet):
    queryset=Breed.objects.all()
    serializer_class=SerializerDetails
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]


#Function Based CRUD operations
@api_view(['GET','POST','PUT','DELETE'])
def dogs_api(request):
    if request.method =='GET':
        id=request.data.get('id')
        if id is not None:
            s=Dog.objects.get(id=id)
            serial=SerializerRecords(s)
            return Response(serial.data)
        s=Dog.objects.all()
        serial=SerializerRecords(s,many=True)
        return Response(serial.data)

    if request.method =='POST':
        serial=SerializerRecords(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Data Created'})
        return Response(serial.errors)

    if request.method =='PUT':
        id=request.data.get('id')
        s=Dog.objects.get(pk=id)
        serial=SerializerRecords(s,data=request.data,partial=True)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Data Updated'})
        return Response(serial.errors)
    
    if request.method=='DELETE':
        id=request.data.get('id')
        s=Dog.objects.get(pk=id)
        s.delete()
        return Response({'msg':'successfully deleted'})

@api_view(['GET','POST','PUT','DELETE'])
def breed_api(request):
    if request.method =='GET':
        id=request.data.get('id')
        if id is not None:
            s=Breed.objects.get(id=id)
            serial=SerializerDetails(s)
            return Response(serial.data)
        s=Breed.objects.all()
        serial=SerializerDetails(s,many=True)
        return Response(serial.data)

    if request.method =='POST':
        serial=SerializerDetails(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Data Created'})
        return Response(serial.errors)

    if request.method =='PUT':
        id=request.data.get('id')
        s=Breed.objects.get(pk=id)
        serial=SerializerDetails(s,data=request.data,partial=True)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Data Updated'})
        return Response(serial.errors)
    
    if request.method=='DELETE':
        id=request.data.get('id')
        s=Breed.objects.get(pk=id)
        s.delete()
        return Response({'msg':'successfully deleted'})


#APIView CRUD Operations
class DogAPIViewLC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Dog.objects.all()
    serializer_class=SerializerRecords

    def get(self,request):
        return self.list(request)
     
    def post(self,request):
        return self.create(request)

class DogAPIViewRDU(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset=Dog.objects.all()
    serializer_class=SerializerRecords

    def get(self,request,**kwargs):
        return self.retrieve(request)

    def delete(self,request,**kwargs):
        return self.destroy(request)

    def put(self,request,**kwargs):
        return self.update(request)

class BreedAPIViewLC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Breed.objects.all()
    serializer_class=SerializerDetails

    def get(self,request):
        return self.list(request)
     
    def post(self,request):
        return self.create(request)

class BreedAPIViewRDU(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset=Breed.objects.all()
    serializer_class=SerializerDetails

    def get(self,request,**kwargs):
        return self.retrieve(request)

    def delete(self,request,**kwargs):
        return self.destroy(request)

    def put(self,request,**kwargs):
        return self.update(request)


#COncrete Generic View CRUD Operations

class DogLCAV(ListCreateAPIView):
    queryset=Dog.objects.all()
    serializer_class=SerializerRecords

class DogRUDAV(RetrieveUpdateDestroyAPIView):
    queryset=Dog.objects.all()
    serializer_class=SerializerRecords

class BreedLCAV(ListCreateAPIView):
    queryset=Breed.objects.all()
    serializer_class=SerializerDetails

class BreedRUDAV(RetrieveUpdateDestroyAPIView):
    queryset=Dog.objects.all()
    serializer_class=SerializerDetails

#ViewSet CRUD operations

class DogViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=Dog.objects.all()
        serializer=SerializerRecords(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            queryset=Dog.objects.get(pk=id)
            serializer=SerializerRecords(queryset)
            return Response(serializer.data)
    
    def update(self,request,pk):
        id=pk
        queryset=Dog.objects.get(pk=id)
        serializer=SerializerRecords(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'successfully updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request):
        id=pk
        queryset=Dog.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'Succesfully deleted'})

    def create(self,request):
        serializer=SerializerRecords(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data created'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BreedViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=Breed.objects.all()
        serializer=SerializerDetails(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            queryset=Breed.objects.get(pk=id)
            serializer=SerializerDetails(queryset)
            return Response(serializer.data)
    
    def update(self,request,pk):
        id=pk
        queryset=Breed.objects.get(pk=id)
        serializer=SerializerDetails(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'successfully updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request):
        id=pk
        queryset=Breed.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'Succesfully deleted'})

    def create(self,request):
        serializer=SerializerDetails(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data created'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Deserialization

@method_decorator(csrf_exempt,name='dispatch')
class Deserialization(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id',None)
        if id is not None:
            s=Dog.objects.get(id=id)
            st=SerializerRecords(s)
            json_data=JSONRenderer().render(st.data)
            return HttpResponse(json_data,content_type='application/json')
        s=Dog.objects.all()
        st=SerializerRecords(s,many=True)
        json_data=JSONRenderer().render(st.data)
        return HttpResponse(json_data,content_type='application/json')
  
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        serializer=SerializerRecords(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        s=Dog.objects.get(id=id)
        serializer=SerializerRecords(s,data=parsed_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        serializer=Dog.objects.get(id=id)
        serializer.delete()
        res={'msg':'Data deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')