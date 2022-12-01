from datetime import date


def get_days_in_month(month, year):

    current = date(year=year, month=month, day=1)

    if month == 12:
        next_month = current.replace(year=current.year+1, month=1)

    else:
        next_month = current.replace(month=current.month+1)

    return (next_month - current).days


print(get_days_in_month(12, 2002))

