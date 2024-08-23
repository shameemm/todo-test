from django.urls import path
from .views import *

urlpatterns = [
    path('task/create/', TaskCreateView.as_view()),
    path('task/update/<id>/', TaskUpdateView.as_view()),
    
    path('todo/',TodoView.as_view()),
    path('todo/update_or_delete/<id>/', TodoUpdateDeleteView.as_view())
]
