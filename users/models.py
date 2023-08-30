from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    city = models.CharField(max_length=100,
                            default="Москва",
                            verbose_name="город")
    phone = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    avatar = models.ImageField(upload_to="users",
                               verbose_name="Аватар",
                               **NULLABLE)
    chat_id = models.IntegerField(default=0, verbose_name="id чата")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
