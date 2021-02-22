from datetime import timedelta

from ariadne import MutationType, QueryType
from ariadne_jwt.decorators import login_required
from habits import models as habit_models

query = QueryType()
mutation = MutationType()


@mutation.field("createDailyHabit")
@login_required
def create_daily_habit(_, info, **data):
    errors = []
    status = False
    user = info.context.get("request").user
    data = data["data"]
    name = data["name"]
    duration_from = data["duration"]["from"]
    duration_to = data["duration"]["to"]
    duration = duration_to - duration_from
    print(duration_from, duration_to, duration)
    if duration_from > duration_to:
        errors.append("The duration can not be negative")
        status = False
    try:
        if habit_models.DailyHabit.objects.filter(name__iexact=name, user=user).exists():
            raise Exception("A habit with this name already exists")
        habit_models.DailyHabit.objects.create(user=user, name=name, duration=duration)
        status = True
    except Exception as exc:
        errors.append(str(exc))
    if not errors:
        errors = None
    return {"status": status, "errors": errors}
