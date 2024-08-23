from django.shortcuts import render
from .models import Tasks,Todo
from .serializers import TaskSerializer, TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class TodoView(APIView):
    """Handles the todo operations"""
    def get(self,request):
        todos = Todo.objects.all()
        print(todos)
        if todos.exists():
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("no data", status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)
    
class TodoUpdateDeleteView(APIView):
    """Handles todo update and delete"""
    
    def put(self,request,*args, **kwargs):
        try:
            id = kwargs.get("id")
            todo = Todo.objects.get(id=id)
            todo.title = request.data.get("title")
            todo.description = request.data.get("description")
            todo.is_deleted = request.data.get("is_deleted")
            return Response(data="Updated", status=status.HTTP_200_OK)
        except Exception as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, *args, **kwargs):
        try:
            id = kwargs.get("id")
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response("Deleted", status=status.HTTP_200_OK)
        except Exception as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
        
class TaskUpdateView(APIView):
    def put(self,request,*args, **kwargs):
        try:
            id = kwargs.get('id')
            task = Tasks.objects.get(id=id)
            task.title = request.data.get("title")
            task.status = request.data.get("status")
            return Response("Task updated", status=status.HTTP_200_OK)
        except Exception as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
        
class TaskCreateView(APIView):
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
        

