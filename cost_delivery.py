def cost_delivery(quantity, *_, discount=0):

    cost = (5 + 2 * (quantity - 1)) * (1 - discount)
    return(cost)
