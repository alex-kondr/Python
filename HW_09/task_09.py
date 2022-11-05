payment = [100, -3, 400, 35, -100]

def positive_values(list_payment):

    positive_payment = []

    for item in filter(lambda number: number > 0, list_payment):
        positive_payment.append(item)

    return positive_payment

print(positive_values(payment))
