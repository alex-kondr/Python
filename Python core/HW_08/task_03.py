from datetime import datetime


date = "2021-05-27 17:08:34.149Z"


def get_str_date(date):

    date = datetime.strptime(date[:10], "%Y-%m-%d")

    return date.strftime("%A %d %B %Y")


get_str_date(date)
