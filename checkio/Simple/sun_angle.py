from typing import Union
import datetime


def sun_angle(time: str) -> Union[int, str]:
    # replace this for solution
    dawn = datetime.datetime.strptime("06:00", "%H:%M")
    sunset = datetime.datetime.strptime("18:00", "%H:%M")
    one_hour = datetime.timedelta(hours=1)
    degree_on_hour = 180 / ((sunset - dawn) / one_hour)

    this_time = datetime.datetime.strptime(time, "%H:%M")
    delta_this_time = (this_time - dawn) / one_hour

    if dawn <= this_time <= sunset:
        return delta_this_time * degree_on_hour

    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("18:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
