"""
Self-contained Django CRUD app (single-file, runnable via: python django_crud.py runserver).
Uses Django REST Framework with an in-memory SQLite DB.

Install: pip install django djangorestframework
"""
import os
import sys
import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="dev-secret-key",
        ALLOWED_HOSTS=["*"],
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "rest_framework",
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        MIDDLEWARE=[
            "django.middleware.common.CommonMiddleware",
        ],
        ROOT_URLCONF=__name__,
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
    )
    django.setup()

from django.db import models
from django.core.management import call_command
from rest_framework import serializers, viewsets, routers
from django.urls import path, include


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()

    class Meta:
        app_label = "django_crud"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "description", "price"]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


router = routers.DefaultRouter()
router.register(r"items", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

if __name__ == "__main__":
    call_command("migrate", "--run-syncdb", verbosity=0)
    call_command("runserver", "8000")
