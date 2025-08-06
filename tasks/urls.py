from django.urls import path, include


from .endpoints import UserViewSet, TaskCreateAPIView, \
    TaskDestroyAPIView, TaskRetrieveAPIView, TaskListAPIView, \
    TasklistCreateAPIView, TaskRetrieveUpdateAPIView, \
    TaskRetrieveDestroyAPIView, TaskRetrieveUpdateDestroyAPIView

from rest_framework import routers

router = routers.SimpleRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("task-list/", TaskListAPIView.as_view()),
    path("task-create/", TaskCreateAPIView.as_view()),
    path("task-detail/<int:pk>/", TaskRetrieveAPIView.as_view()),
    path("task-destroy/<int:pk>/", TaskDestroyAPIView.as_view()),
    path("task-list-create/", TasklistCreateAPIView.as_view()),
    path("task-detail-update/<int:pk>/", TaskRetrieveUpdateAPIView.as_view()),
    path("task-detail-destroy/<int:pk>/", TaskRetrieveDestroyAPIView.as_view()),
    path("task-detail-update-destroy/<int:pk>/", TaskRetrieveUpdateDestroyAPIView.as_view()),

    path("", include(router.urls))
]