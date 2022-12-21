from datetime import datetime, timedelta


def get_birthdays_per_week(users: list) -> dict:

    birth_users = {}

    for user in users:

        day = day_of_celebration(user["birthday"])

        if day and birth_users.get(day):
            birth_users[day].append(user["name"])

        elif day:
            birth_users[day] = [user["name"]]

    return birth_users

def day_of_celebration(birthday: datetime) -> str:
    # If birthday is the next week returns day of week

    day = ""

    now = datetime.now()
    next_week = now + timedelta(weeks=1)
    birthday = birthday.replace(year=now.year)    

    if birthday.isocalendar().week == next_week.isocalendar().week and \
        birthday.weekday() not in (5, 6):

        day = birthday.strftime("%A")

    elif birthday.isocalendar().week == now.isocalendar().week and \
        birthday.weekday() in (5, 6):
       
        day = "Monday"

    return day

