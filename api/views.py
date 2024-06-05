from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *


# ======================================= REST FRAMEWORK AUTH  -================================

@api_view(['POST'])
def signup(request):
    serializer = Auth(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        userA = User.objects.get(username=request.data['username'])
        token = Token.objects.create(user=userA)
        
        
        serializer = Auth(userA)
        
        context = {
            "user": serializer.data,
            "token": token.key
        }
        return Response(context, status=status.HTTP_201_CREATED)

    
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def login(request):
    
    return Response({"Success": "Login to your account"})

@api_view(['GET'])
def testView(request):
    
    return Response({"Success": "Test your account"})

@api_view(['POST'])
def logout(request):
    
    return Response({"Success": "Logout your account"})




# ======================================= API CRUD WITH REST FRAMEWORK -================================
@api_view(['GET'])
def index(request):
    
    return Response({"Success":"The Setup was successful."})


@api_view(['GET'])
def get_post(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True) #The many=True will tell django we are passing a queary set(A list of object into the serializers)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def createPost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "Post created Successfully"}, status=201)
    else:
        return Response(serializer.errors, status=400)
    
    
@api_view(['DELETE'])
def deletePost(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Success": f"POst No.{post_id} Deleted Successfully"})
    except Post.DoesNotExist:
        return Response({f"Post No.{post_id} does not exist."})
    
    
@api_view(['GET'])
def getPost(request):
    post = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"Error": "Not Valid id"})
    

@api_view(['PUT'])
def updatePost(request):
    post_id = request.data.get('post_id')
    titleN = request.data.get('titleN')
    contentN = request.data.get("contentN")
    
    try:
        post = Post.objects.get(id=post_id)
        
        if titleN:
            post.title = titleN
            
        if contentN:
            post.content = contentN
            
        post.save()
        return Response({"Success": "post updated successful"})
    
    
    except Post.DoesNotExist:
        return Response({"Error": "The Post does not exist"})