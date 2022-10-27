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

users1 = []

def get_birthdays_per_week(users):

    birth_users = {}
    now = datetime.now()
    next_week = now + timedelta(weeks=1)
    week = timedelta(weeks=1)

    for u in users:
        a = u["birthday"]
        b = next_week.weekday()
        temp = datetime(year=now.year, month=u["birthday"].month, day=u["birthday"].day)

        if temp.isocalendar().week == next_week.isocalendar().week:

            if birth_users.get(temp.strftime("%A")):
                birth_users[temp.strftime("%A")].append(u["name"])
            else:
                birth_users[temp.strftime("%A")] = [u["name"]]

        elif temp.isocalendar().week == now.isocalendar().week and \
                (temp.weekday() == 5 or temp.weekday() == 6):

            if birth_users.get("Monday"):
                birth_users["Monday"].append(u["name"])
            else:
                birth_users["Monday"] = [u["name"]]

    return birth_users

print(get_birthdays_per_week(users1))



