from django.db import models
from datetime import datetime, timedelta
from django.db.models import Q
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


def save(self, *args, **kwargs):
    duplicated_alias = Alias.objects.filter(
        Q(alias=self.alias), Q(target=self.target), Q(end__isnull=True)
    )
    if duplicated_alias.exists():
        raise ValidationError("Same active alias exists.")
    else:
        super(Alias, self).save(*args, **kwargs)


def to_end_alias(self, *args, **kwargs):
    end = datetime.now() - timedelta(microseconds=1)
    self.end = end
    super(Alias, self).save(*args, **kwargs)
    return self.end