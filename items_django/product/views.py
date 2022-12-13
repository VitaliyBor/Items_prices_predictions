from os import kill
from django.db.models import Q,When,Case,IntegerField
from django.http import Http404
from rest_framework import serializers
from django.shortcuts import get_object_or_404



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from colabFiltration import run 
from forecasting import run_2 
import pandas as pd
import csv 
import os.path 


from .models import Product, Category,Review,Hotel, Item
from .serializers import ProductSerializer, CategorySerializer,HotelsSerializer,ItemSerializer
 #os.path.join(path, "User/Desktop", "file.txt")


class LatestProductsList(APIView):
    def get(self, request, format=None):
        #request.GET["firstName"]
        #print(self.request.firstName)
        #print(self.request.lastName)
        #products = Product.objects.all()[0:4]
        #serializer = ProductSerializer(products)


        # old
        # hotels = Hotel.objects.all()[0:8]
        # serializer = HotelsSerializer( hotels, many=True)
        
        #new
        items = Item.objects.all()[0:8]
        serializer = ItemSerializer( items, many=True)

        return Response(serializer.data)

class RecomendationList(APIView):
    def get(self, request,input_id, format=None):
        
        products = Product.objects.all()[0:4]
        hotels = Hotel.objects.all()[0:8]
        reviews= Review.objects.all() 
            # with open("eggs.csv", 'w', newline='') as csvfile:
            #  spamwriter = csv.writer(csvfile, delimiter=',' )
        #  test 29.11 start code
        print("hotal")
        print( str(hotels[0]))
        file_name = str(hotels[0])+'.csv'
        with open(file_name, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))

        #  test 29.11 end code
        r=[]
        for revie in reviews:
           r.append([ str(revie.user_id), str(revie.hotel_id), str(revie.mark)])
        # f = open ("eggs.csv")
        # r = csv.reader (f)
        print(input_id)
        answer =run(r,'4',5,5)  # [('1', 4.266562464027468), ('2', 3.0750917799698136), ('3', 2.6257924124161804)]
         #f.close()
        order = [id for (id,_) in answer]
        
        # finalAnwer = Product.objects.filter(id__in=result).order_by('-timestamp')
        # from django.db import models
    
        # order = ['b', 'a', 'z', 'x', 'c']
        whens = []
        for sort_index, value in enumerate(order):
            whens.append(When(id=value, then=sort_index))
        
        qs = Hotel.objects.annotate(_sort_index=Case(*whens, output_field=IntegerField()))

        serializer = HotelsSerializer( qs.order_by('_sort_index').filter(pk__in=order), many=True)
        
        print(serializer.data) 
         #serializer = HotelsSerializer(hotels, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404  
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class TetsDetails(APIView):
    def get(self, request,username,input_id, format=None):
        #request.GET["firstName"]
        #print(self.request.firstName)
        #print(self.request.lastName)
        #products = Product.objects.all()[0:4]
        #serializer = ProductSerializer(products)
        print(input_id)
        print(username)
        
        # hotel =  Hotel.objects.get(pk=input_id)
        # hotels = Hotel.objects.all()[0:8]
        # serializer = HotelsSerializer( hotel)
        file_name = str(input_id)+'.csv'

        mse,rmse,price, date = run_2(file_name)
        item =  Item.objects.get(pk=input_id)
        # print(dir (item))
        item.minprice = price
        item.mindate = date
        item.mse = mse
        item.rmse = rmse
        serializer = ItemSerializer( item)
        return Response(serializer.data)


@api_view(['POST'])
def addReview(request ):
    # print(request.body)
    r= Review(name = request.data['name'],mark = request.data['mark'], user_id_id = request.data['user_id'], hotel_id_id =request.data['hotel_id'] )
    r.save()
    return Response('Review was created')

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})