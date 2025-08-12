from rest_framework import permissions, viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListCreateAPIView, RetrieveAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from .sql_tests import (get_all_tasks, in_progress_into_completed,
                        new_into_in_progress, tasks_by_status,
                        tasks_in_progress, tasks_is_completed)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = [permissions.AllowAny]


# working with one element


class TaskRetrieveAPIView(RetrieveAPIView):  # get one
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateAPIView(CreateAPIView):  # create one
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateAPIView(RetrieveUpdateAPIView):  # update a certain task #
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView):  # delete one
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# showing the list
class TaskListSQLAPIView(APIView):  # get the list with all tasks
    def get(self, request):
        return Response(get_all_tasks())


class TaskInProgressSQLAPIview(APIView):  # get the list with tasks in progress
    def get(self, request):
        return Response(tasks_in_progress())


class TaskCompletedSQLAPIview(APIView):  # get the list with completed status
    def get(self, request):
        return Response(tasks_is_completed())


class TaskInprogressIntoCompletedSQLAPIview(
    APIView
):  # turn status inProgress into Completed
    def post(self, request):
        updated = in_progress_into_completed()
        return Response({"updated": updated})


class TaskNewIntoInProgressSQLAPIview(APIView):  # turn status new into inProgress
    def post(self, request):
        updated = new_into_in_progress()
        return Response({"updated": updated})


class CountTaskByStatusSQLAPIview(APIView):  # how many tasks of certain status
    def get(self, request):
        return Response(tasks_by_status())


# working with the list of elements
class TasklistCreateAPIView(ListCreateAPIView):  # create the list of tasks
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveDestroyAPIView(RetrieveDestroyAPIView):  # delete one task
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
