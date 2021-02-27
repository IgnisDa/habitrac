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
@convert_kwargs_to_snake_case
@login_required
def create_daily_habit(_, info, data):
    error_container = ErrorContainer("date_from", "date_to", "name")
    status = False
    habit = None
    user = get_user(info)
    name = data.get("name")
    description = data.get("description")
    date_from = data.get("date_from")
    date_to = data.get("date_to")
    today = datetime.date.today()
    if date_from < today:
        error_container.update_with_error(
            "date_from",
            f"The starting date must be greater than {today.strftime('%m/%d/%Y')}",
        )
    if date_to - date_from < datetime.timedelta(days=0):
        error_container.update_with_error(
            "date_to", "The ending date can not be before the ending date"
        )
    if habit_models.DailyHabit.objects.filter(name__iexact=name, user=user).exists():
        error_container.update_with_error(
            "name", "A habit with this name already exists"
        )
    if not error_container:
        habit = habit_models.DailyHabit.objects.create(
            user=user,
            name=name,
            date_from=date_from,
            date_to=date_to,
            description=description,
        )
        status = True
    return {"status": status, "errors": error_container.get_all_errors(), "habit": habit}


@mutation.field("updateDailyHabit")
@convert_kwargs_to_snake_case
@login_required
def update_daily_habit(_, info, data, name_slug):
    error_container = ErrorContainer("duration", "name", "name_slug")
    status = False
    habit = None
    name = data.get("name")
    user = get_user(info)
    description = data.get("description")
    duration_to = data.get("duration").get("to")
    habits = habit_models.DailyHabit.objects.filter(name_slug=name_slug, user=user)
    if len(habits) > 1:
        error_container.update_with_error(
            "name_slug", "There was an error processing your request"
        )
    if not habits.exists():
        error_container.update_with_error(
            "name_slug", "The habit you requested for does not exist"
        )
    if not error_container:
        habit = habits[0]
        habit.name = name
        habit.description = description
        # duration = (duration_to - habit.started_on).total_seconds() // (3600 * 24)
        duration_obj = duration_to.date() - habit.started_on + datetime.timedelta(days=1)
        habit.duration = duration_obj
        habit.save()
        status = True
    return {"status": status, "errors": error_container.get_all_errors(), "habit": habit}


@query.field("getAllHabits")
@convert_kwargs_to_snake_case
@login_required
def get_all_habits(_, info, username_slug, **kwargs):
    qs = CUSTOM_USER_MODEL.objects.get(username_slug=username_slug).dailyhabit_set.all()
    ret_value = []
    for obj in qs:
        vars(obj)["is_completed"] = obj.is_completed
        vars(obj)["is_done"] = obj.is_done
        obj.progress = json.dumps(obj.progress)
        ret_value.append(vars(obj))
    return ret_value


@query.field("getHabitDetails")
@convert_kwargs_to_snake_case
@login_required
def get_habit_details(_, info, name_slug, **kwargs):
    error = None
    user = get_user(info)
    ret_value = None
    try:
        habit = habit_models.DailyHabit.objects.get(name_slug=name_slug, user=user)
        vars(habit)["is_completed"] = habit.is_completed
        vars(habit)["is_done"] = habit.is_done
        habit.is_done
        habit.progress = json.dumps(habit.progress)
        ret_value = vars(habit)
    except habit_models.DailyHabit.DoesNotExist:
        error = "The habit you requested for does not exist"
    return {"habit": ret_value, "error": error}


@mutation.field("toggleTagCycle")
@convert_kwargs_to_snake_case
@login_required
def toggle_tag_cycle(_, info, data, **kwargs):
    status = False
    error = None
    user = get_user(info)
    habit = habit_models.DailyHabit.objects.get(name_slug=data["name_slug"], user=user)
    try:
        today = data.get("date").strftime("%Y-%m-%d")
        habit.toggle_day(today)
        habit.save()
        status = True
    except KeyError:
        error = "The day you're trying to mark does not fall in this habit's duration."
    return {"status": status, "error": error}
