def amount_payment(payment):
    score = 0
    for element in payment:
        if element > 0:
            score += element

    return score
    