from rest_framework import serializers
from .models import Todo, Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        
class TodoSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        fields = '__all__'
    
    def get_tasks(self,todo):
        """retrun the task key value fro task table"""
        if todo:
            tasks = Tasks.objects.filter(todo=todo)
            
            return TaskSerializer(tasks, many=True).data
        
        
