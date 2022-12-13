from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)


        if not serializer.is_valid():
            return Response({'status' : 403 ,'errors' : serializer.errors, 'message' : 'something went wrong'})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        user = User.objects.get(password = serializer.data['password'])
        token_obj , _ =Token.objects.get_or_create(user=user)
        return Response({'status' : 200 , 'payload' : serializer.data , 'token' : str(token_obj), 'message' : 'your data is saved'})
        



class EbookAPIView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    


    def get(self,request):
        ebooks = Ebook.objects.all() #complex query set
        serializer = EbookSerializer(ebooks, many=True) #python native datatype(dictionary)
        return Response(serializer.data)#return json response

    def post(self,request):
        serializer = EbookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTp_400_BAD_REQUEST)  
        

class EbookDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self,id):
        try:
            return Ebook.objects.get(id=id)
        except Ebook.DoesNotExist:
            return HttpResponse(status=status.Http_404_NOT_FOUND)      

    def get(self, request, id):
        ebook = self.get_object(id)
        serializer = EbookSerializer(ebook)
        return Response(serializer.data)   
            
    def put(self, request, id):
        ebook = self.get_object(id)
        serializer = EbookSerializer(ebook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class filterEbook(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        ebooks = Ebook.objects.filter(favorite=True) #complex query set
        serializer = EbookSerializer(ebooks, many=True) #python native datatype(dictionary)
        return Response(serializer.data)        
