from enum import unique
from .managers import CustomUserManager
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import \
    gettext_lazy as _


class DataTimeMixin:
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

class User(AbstractBaseUser, DataTimeMixin, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")



class Task(models.Model):
    STATUS = (("new", "New"), ("in_progress", "In progress"), ("completed", "Completed"))
    task_name = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default="New")

    def __str__(self):
        return f"{self.pk} - {self.task_name}"

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")





