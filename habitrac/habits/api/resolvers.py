import datetime
import json

from ariadne import MutationType, QueryType, convert_kwargs_to_snake_case
from ariadne_token_auth.decorators import login_required
from django.contrib.auth import get_user_model
from habits import models as habit_models
from utils.general import get_user
from utils.handlers.errors import ErrorContainer

CUSTOM_USER_MODEL = get_user_model()
query = QueryType()
mutation = MutationType()


@mutation.field("createDailyHabit")
@login_required
def create_daily_habit(_, info, **data):
    error_container = ErrorContainer("duration", "name")
    status = False
    habit = None
    user = info.context.get("request").user
    data = data["data"]
    name = data["name"]
    duration_from = data["duration"]["from"]
    duration_to = data["duration"]["to"]
    now = datetime.datetime.now() - datetime.timedelta(days=1)
    if duration_from < now:
        error_container.update_with_error(
            "duration",
            f"The starting date must be greater than {now.strftime('%m/%d/%Y')}",
        )
    duration_obj = duration_to - duration_from
    duration = (duration_to - duration_from).total_seconds() // (3600 * 24)
    if duration == 0:
        error_container.update_with_error(
            "duration", "The starting date and the ending date can not be same"
        )
    elif duration < 0:
        error_container.update_with_error(
            "duration", "The starting date can not be after the ending date"
        )
    if habit_models.DailyHabit.objects.filter(name__iexact=name, user=user).exists():
        error_container.update_with_error(
            "name", "A habit with this name already exists"
        )
    if not error_container:
        habit = habit_models.DailyHabit.objects.create(
            user=user, name=name, duration=duration_obj
        )
        status = True
    return {"status": status, "errors": error_container.get_all_errors(), "habit": habit}


@query.field("getAllHabits")
@convert_kwargs_to_snake_case
@login_required
def get_all_habits(_, info, username_slug, **kwargs):
    qs = CUSTOM_USER_MODEL.objects.get(username_slug=username_slug).dailyhabit_set.all()
    for obj in qs:
        obj.progress = json.dumps(obj.progress)
    return qs


@query.field("getHabitDetails")
@convert_kwargs_to_snake_case
@login_required
def get_habit_details(_, info, name_slug, **kwargs):
    error = None
    habit = None
    user = get_user(info)
    try:
        habit = habit_models.DailyHabit.objects.get(name_slug=name_slug, user=user)
        habit.progress = json.dumps(habit.progress)
    except habit_models.DailyHabit.DoesNotExist:
        error = "The habit you requested for does not exist"
    return {"habit": habit, "error": error}


@mutation.field("toggleTagCycle")
@convert_kwargs_to_snake_case
@login_required
def toggle_tag_cycle(_, info, data, **kwargs):
    status = False
    error = None
    user = get_user(info)
    habit = habit_models.DailyHabit.objects.get(name_slug=data["name_slug"], user=user)
    try:
        habit.progress[f"cycle-{data['cycle_index']}"] = not habit.progress[
            f"cycle-{data['cycle_index']}"
        ]
        habit.save()
        status = True
    except KeyError:
        error = "Incorrect index specified. Make sure they are 1 indexed."
    return {"status": status, "error": error}
