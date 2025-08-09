from django.urls import path, include


from .endpoints import UserViewSet, TaskCreateAPIView, \
    TaskDestroyAPIView, TaskRetrieveAPIView, TaskListSQLAPIView, \
    TasklistCreateAPIView, TaskRetrieveUpdateAPIView, \
    TaskRetrieveDestroyAPIView, TaskRetrieveUpdateDestroyAPIView, TaskInProgressSQLAPIview, \
    TaskInprogressIntoCompletedSQLAPIview, \
    TaskNewIntoInProgressSQLAPIview, CountTaskByStatusSQLAPIview, TaskCompletedSQLAPIview

from rest_framework import routers

router = routers.SimpleRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("task-list/", TaskListSQLAPIView.as_view()),
    path("in-progress/", TaskInProgressSQLAPIview.as_view()),
    path("completed/", TaskCompletedSQLAPIview.as_view()),
    path("progress-completed/", TaskInprogressIntoCompletedSQLAPIview.as_view()),
    path("new-progress/", TaskNewIntoInProgressSQLAPIview.as_view()),
    path("count-by-status/", CountTaskByStatusSQLAPIview.as_view()),
    path("task-create/", TaskCreateAPIView.as_view()),
    path("task-detail/<int:pk>/", TaskRetrieveAPIView.as_view()),
    path("task-destroy/<int:pk>/", TaskDestroyAPIView.as_view()),
    path("task-list-create/", TasklistCreateAPIView.as_view()),
    path("task-detail-update/<int:pk>/", TaskRetrieveUpdateAPIView.as_view()),
    path("task-detail-destroy/<int:pk>/", TaskRetrieveDestroyAPIView.as_view()),
    path("task-detail-update-destroy/<int:pk>/", TaskRetrieveUpdateDestroyAPIView.as_view()),

    path("", include(router.urls))
]


