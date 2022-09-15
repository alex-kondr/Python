def game(terra, power):

    total_power = power

    for i in range(len(terra)):
        
        for item_power in terra[i]:          

            if total_power >= item_power:
                total_power += item_power
            else:
                break

    return total_power

