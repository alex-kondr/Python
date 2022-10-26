from datetime import datetime, timedelta


users = [
    {"name": "Bill+", "birthday": datetime(year=2002, month=11, day=3)},
    {"name": "Jill+", "birthday": datetime(year=1996, month=10, day=30, hour=10, minute=32)},
    {"name": "Kim+", "birthday": datetime(year=2005, month=11, day=1)},
    {"name": "Jan+", "birthday": datetime(year=2007, month=10, day=30, hour=6)},
    {"name": "Foo", "birthday": datetime(year=1997, month=8, day=2)},
    {"name": "Bar", "birthday": datetime(year=2009, month=1, day=14)},
    {"name": "Baz+", "birthday": datetime(year=1989, month=10, day=29, hour=18, minute=31, second=46)}
]

users1 = []

def get_birthdays_per_week(users):

    birth_users = {}
    now = datetime.now()
    next_week = now + timedelta(weeks=1)

    for u in users:
        a = u["birthday"].weekday()
        b = next_week.weekday()

        if u["birthday"].weekday() == next_week.weekday():

            if birth_users.get(u["birthday"].strftime("%A")):
                birth_users[u["birthday"].strftime("%A")].append(u["name"])
            else:
                birth_users[u["birthday"].strftime("%A")] = [u["name"]]

        elif u["birthday"].weekday() == now.weekday() and \
            (u["birthday"].strftime("%w") == 5 or u["birthday"].strftime("%w") == 6):

            if birth_users.get("Monday"):
                birth_users["Monday"].append(u["name"])
            else:
                birth_users["Monday"] = [u["name"]]

    return birth_users

print(get_birthdays_per_week(users))



