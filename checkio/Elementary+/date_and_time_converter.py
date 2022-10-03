from datetime import datetime

def date_time(time: str) -> str:
    # replace this for solution
    time = datetime.strptime(time, "%d.%m.%Y %H:%M")
    hour_s = "hour" if time.hour == 1 else "hours"
    minute_s = "minute" if time.minute == 1 else "minutes"

    return f"{time.day} {time.strftime('%B')} {time.year} year {time.hour} {hour_s} {time.minute} {minute_s}"


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("09.07.1995 16:01") == "9 July 1995 year 16 hours 1 minute"
    ), "Millenium"
    assert (
        date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
