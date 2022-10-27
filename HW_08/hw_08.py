from datetime import datetime, timedelta


def get_birthdays_per_week(users: list) -> dict:

    birth_users = {}

    for u in users:

        day = day_of_celebration(u["birthday"])

        if day and birth_users.get(day):
            birth_users[day].append(u["name"])

        elif day:
            birth_users[day] = [u["name"]]

    return birth_users


def day_of_celebration(byrthday: datetime) -> str:
    # If birthday is the next week returns day of week

    day = ""

    now = datetime.now()
    next_week = now + timedelta(weeks=1)
    birthday = datetime(
        year=now.year, 
        month=byrthday.month,
        day=byrthday.day
    )

    if birthday.isocalendar().week == next_week.isocalendar().week:

        day = birthday.strftime("%A")

    elif birthday.isocalendar().week == now.isocalendar().week and \
        (birthday.weekday() == 5 or birthday.weekday() == 6):
       
        day = "Monday"

    return day

