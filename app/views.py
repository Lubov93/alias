import datetime
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Alias, Object


def referred_obj_slug(alias, end=None):
    alias_obj = Alias.objects.filter(alias=alias)
    if alias_obj:
        if end is not None:
            return [i.target.name for i in alias_obj.filter(end__lte=end)]
        else:
            return [i.target.name for i in alias_obj.filter(end__isnull=True)]
        raise ValidationError("Alias is not found")


def get_aliases(target, from_time, to_time):
    try:
        target_obj = Object.objects.get(name=target)
    except Object.DoesNotExist:
        raise Object.DoesNotExist(f"Targeted object - {target} - does not exist")

    else:
        if (type(from_time) is datetime.datetime) \
                and (type(to_time) is datetime.datetime):
            alias_unfiltered = Alias.objects.filter(target=target_obj.id)
            if alias_unfiltered.exists():
                if (Alias.objects.filter(Q(target=target_obj.id),
                                         Q(start__lte=to_time),
                                         Q(end__gte=from_time)).exists()
                        or Alias.objects.filter(Q(target=target_obj.id),
                                                Q(start__lte=to_time),
                                                Q(end__isnull=True)).exists()):
                    alias_list = [i.alias for i in alias_unfiltered]
                    return f"Targeted aliases are: {alias_list}"
                raise ValidationError(f"No aliases with {target} target"
                                      f" were active at that time")
            raise ValidationError(f"Alias objects with {target} don't exist")
        raise TypeError(f"from_time ({from_time}) or to_time ({to_time})"
                        f" parameters are not in DateTime format")



def replace_alias(existing_alias_id, replace_at, new_alias_value):
    if type(replace_at) is datetime.datetime:
        alias = Alias.objects.get(id=existing_alias_id)
        if alias.start.replace(tzinfo=None) >= replace_at:
            raise ValidationError(
                f"Replacement of {alias.id} with {alias.start} is impossible: "
                f"start time is greater than replace_at"
            )
        else:
            # Updating existing Alias
            Alias.objects.filter(pk=alias.pk).update(end=replace_at)
            alias.refresh_from_db()
            print(f"Alias object updated: {alias.__dict__}")

            # Creating new Alias
            new_alias = Alias.objects.create(
                alias=new_alias_value, target=alias.target, start=replace_at)
            print(f"New alias object created:{new_alias.__dict__}")
            return f"Done! New alias id is {new_alias.id}"

    raise TypeError(f"replace_at ({replace_at}) parameter "
                    f"is not in DateTime format")
