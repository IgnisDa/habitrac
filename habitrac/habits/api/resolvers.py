from ariadne import MutationType, QueryType
from ariadne_jwt.decorators import login_required

query = QueryType()
mutation = MutationType()


@mutation.field("createDailyHabit")
# @login_required
def create_daily_habit(*_, **data):
    print(data)
    return {"status": True}
