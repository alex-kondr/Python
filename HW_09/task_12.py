from functools import reduce


def amount_payment(payment):

    positive_payment = []

    for item in filter(lambda payment: payment > 0, payment):
        positive_payment.append(item)

    return reduce(lambda x, y: x + y, positive_payment)
