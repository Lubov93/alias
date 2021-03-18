from django.db import models
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError


class Object(models.Model):
    name = models.CharField(null=False, max_length=24, unique=True)

    def __str__(self):
        return self.name


class Alias(models.Model):
    alias = models.CharField(null=False, max_length=255)
    target = models.ForeignKey(Object, db_constraint=False,
                               on_delete=models.DO_NOTHING)
    start = models.DateTimeField(auto_now=True)
    end = models.DateTimeField(null=True)

    def __str__(self):
        return self.alias