from rest_framework.serializers import ModelSerializer
from .models import User, Task

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
