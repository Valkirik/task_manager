from rest_framework import permissions, viewsets
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = [permissions.AllowAny]


#working with one element
class TaskCreateAPIView(CreateAPIView): #create one
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView): #delete one
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveAPIView(RetrieveAPIView): #get one
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


#showing the list
class TaskListAPIView(ListAPIView): #get the lise
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


#working with the list of elements
class TasklistCreateAPIView(ListCreateAPIView): #create the list of tasks
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateAPIView(RetrieveUpdateAPIView): #
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


