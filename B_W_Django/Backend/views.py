from .serializers import regSerializer,UserSerializer
from .models import reg
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer # for json render
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework.decorators import api_view, permission_classes

from rest_framework.authentication import TokenAuthentication  # <-- Here


from rest_framework import viewsets # for class view set 
#-------------------------------------knowing about ListCreateAPIView---------------------------
#Our view has a very commonly occuring pattern where we want to create an instance of a model and want to provide representation of all instances of a model. We had to provide a get() and post() implementation to achieve this.

#ListCreateAPIView provides a default implementation of get() and post(). It requires two mandatory attributes which are serializer_class and queryset.

#Let’s modify the QuestionsView to use ListCreateAPIView

#def registeration(request):
 #   re_queryset=reg.objects.all()

  #  re_serializer=regSerializer(re_queryset,many=True)
   # re_json_data=JSONRenderer().render(re_serializer.data)
  #  return HttpResponse(re_json_data,content_type='application/json')
#class regCreate(generics.ListCreateAPIView):
 #   queryset = reg.objects.all()
  #  serializer_class = regSerializer
#----------------------knowing about RetrieveUpdateDestroyAPIView--------------------------------
#Our view has a very commonly occuring pattern where we want to see detail of a model instance, want to edit a model instance and delete a model instance. We had to provide a get(), patch() and delete() implementation to achieve this.
#RetrieveUpdateDestroyAPIView provides a default implementation of get(), patch() and delete(). RetrieveUpdateDestroyAPIView requires two mandatory attributes which are serializer_class and queryset. There is another optional attribute called lookup_url_kwarg which might be needed depending on your url pattern.
#class regDetail(generics.RetrieveUpdateDestroyAPIView):
 #   queryset = reg.objects.all()
  #  serializer_class = regSerializer
# @api_view - Wrapping API view of rest frameowrk or API decortator
@api_view(['GET', 'POST'])# is handling both GET and POST operations over the root endpoint of our API. This means every time we make a request over http://localhost:8000/api/students with GET and POST HTTP verbs, we’ll execute this method.
@permission_classes([IsAuthenticated]) # so after add it you cannot  access this view without authentication 
def User_detail(request): #function based API
    if request.method == 'GET':
        data = reg.objects.all() # retrive complex datatype

        serializer = regSerializer(data, many=True) # convert into python dic using serializer this process is called serialization

        return Response(serializer.data) #return reponse in json

    elif request.method == 'POST':
        serializer = regSerializer(data=request.data) # get json data from frontend in request.data and pass to serializer for convert into python datatype this process is called deseralization
       # we’re first calling the is_valid() method on the serializer to ensure that the data received is conformed with our model.
        if serializer.is_valid(): # after deseralization checking if it valid format.
            serializer.save() # save python datatype into model instance into table.
            return Response(serializer.data) #send responce
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # if data not valid return 404 page
@api_view(['PUT', 'DELETE','GET']) # here specifiy which operation you want to perform in below API. IF YOU REMOVE any of PUT,Get <delete method 
#put mean update
# delete mean delete
@permission_classes([IsAuthenticated]) ## so after add it you cannot  access this view without authentication  for detail  read sitting.py file

# when you call get method from frontend it generate error so mention here its compolsoury task. so it called api view.

# Its for update and detele particular table's row data based on key

def User_upadte(request, pk):
    try:
        data = reg.objects.get(pk=pk)
    except reg.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=='GET': # if it get request to give the particular key data 
            serializer = regSerializer(data) # convert into python dic using serializer this process is called serialization
            return Response(serializer.data)


    if request.method == 'PUT': # if it update request
        # its same just above
        serializer = regSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': # if it delete request
        data.delete() # delete instance of model based PK
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# iits user authenticate and create api function
# here we are not using authentication permission class.
@api_view(['GET', 'POST'])# is handling both GET and POST operations over the root endpoint of our API. This means every time we make a request over http://localhost:8000/api/students with GET and POST HTTP verbs, we’ll execute this method.
def User_Auth_detail(request): #function based API
    if request.method == 'GET':
        data = User.objects.all() # retrive complex datatype

        serializer = UserSerializer(data, many=True) # convert into python dic using serializer this process is called serialization

        return Response(serializer.data) #return reponse in json

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data) # get json data from frontend in request.data and pass to serializer for convert into python datatype this process is called deseralization
        #print(serializer.data)
       # we’re first calling the is_valid() method on the serializer to ensure that the data received is conformed with our model.
        if serializer.is_valid(): # after deseralization checking if it valid format.

            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



# for testing purpose ignor it.
@api_view(['GET', 'POST'])
def test(request):
    if(request.method=='GET'):
        var=['puneet','singh','rajput','yes','no']
        var1=['no1,no2,no3,no4']
        var3=['yes1','yes2','yes3','yes4','yes5','yrd56']
        data_dic={'variables':var,'heading':var1,'paragraphs':var3}
        import json
        app_json = json.dumps(data_dic)
        return Response(app_json,status=status.HTTP_200_OK)



