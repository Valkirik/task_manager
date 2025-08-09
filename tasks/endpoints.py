from rest_framework import permissions, viewsets
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .sql_tests import get_all_tasks, tasks_in_progress, tasks_is_completed, in_progress_into_completed, \
    new_into_in_progress, tasks_by_status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = [permissions.AllowAny]


#working with one element
class TaskCreateAPIView(CreateAPIView): #create one
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView): #delete one
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveAPIView(RetrieveAPIView): #get one
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


#showing the list
class TaskListSQLAPIView(APIView): #get the lise
    def get(self, request):
        return Response(get_all_tasks())

class TaskInProgressSQLAPIview(APIView):
    def get(self, request):
        return Response(tasks_in_progress())

class TaskCompletedSQLAPIview(APIView):
    def get(self, request):
        return Response(tasks_is_completed())

class TaskInprogressIntoCompletedSQLAPIview(APIView):
    def post(self, request):
        updated = in_progress_into_completed()
        return Response({"updated": updated})

class TaskNewIntoInProgressSQLAPIview(APIView):
    def post(self, request):
        updated = new_into_in_progress()
        return Response({"updated": updated})

class CountTaskByStatusSQLAPIview(APIView) :
    def get(self, request):
        return Response(tasks_by_status())


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


