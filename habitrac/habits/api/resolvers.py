from ariadne import MutationType, QueryType
from ariadne_token_auth.decorators import login_required
from habits import models as habit_models

query = QueryType()
mutation = MutationType()


@mutation.field("createDailyHabit")
@login_required
def create_daily_habit(_, info, **data):
    errors = {}
    status = False
    user = info.context.get("request").user
    data = data["data"]
    name = data["name"]
    duration_from = data["duration"]["from"]
    duration_to = data["duration"]["to"]
    duration_obj = duration_to - duration_from
    duration = (duration_to - duration_from).total_seconds() // (3600 * 24)
    if duration == 0:
        errors.update(
            {"duration": ["The starting date and the ending date can not be same"]}
        )
        status = False
    elif duration < 0:
        errors.update(
            {"duration": ["The starting date can not be after the ending date"]}
        )
        status = False
    if habit_models.DailyHabit.objects.filter(name__iexact=name, user=user).exists():
        errors.update({"name": ["A habit with this name already exists"]})
    else:
        habit_models.DailyHabit.objects.create(
            user=user, name=name, duration=duration_obj
        )
    if not errors:
        errors = None
        status = True
    return {"status": status, "errors": errors}
