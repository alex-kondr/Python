from random import randrange


def get_numbers_ticket(min, max, quantity):

    r = []

    if min < quantity < max and min > 0 and max < 1000:

        while len(r) < quantity:
            number = randrange(min, max)

            if number not in r:
                r.append(number)

    r.sort()

    return r

print(get_numbers_ticket(-1, 10, 5))
