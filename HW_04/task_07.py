points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):

    distance = 0

    if coordinates:

        for i in range(len(coordinates)):

            if i >= 1:

                point = (coordinates[i-1], coordinates[i]) if coordinates[i -
                    1] <= coordinates[i] else (coordinates[i], coordinates[i-1])

                distance += points.get(point, 0)

    return distance

