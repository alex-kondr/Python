from datetime import datetime, timedelta


users = [
    {"name": "Bill+", "birthday": datetime(year=2002, month=11, day=3)}, #Thursday
    {"name": "Jill+", "birthday": datetime(year=1996, month=10, day=30, hour=10, minute=32)}, #Monday
    {"name": "Kim+", "birthday": datetime(year=2005, month=11, day=1)}, #Tuesday
    {"name": "Jan+", "birthday": datetime(year=2007, month=10, day=30, hour=6)}, #Monday
    {"name": "Foo", "birthday": datetime(year=1997, month=8, day=2)}, #-
    {"name": "Bar", "birthday": datetime(year=2009, month=1, day=14)}, #-
    {"name": "Baz+", "birthday": datetime(year=1989, month=10, day=29, hour=18, minute=31, second=46)} #Monday
]


def get_birthdays_per_week(users):

    birth_users = {}

    for u in users:

        day, name = add_to_calendar(u["name"], u["birthday"])

        if day and birth_users.get(day):
            birth_users[day].append(name)

        elif day:
            birth_users[day] = [name]

    return birth_users

def add_to_calendar(name: str, byrthday: datetime):

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

    return day, name


print(get_birthdays_per_week(users))



