def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    """
    TOP most expensive goods
    """
    # your code here
    
    data_temp = data.copy()
    price_bigger = []    

    def bigger_item(data: list[dict]):

        price = 0

        for item in data:

            if price < item["price"]:
                price = item["price"]
                bigger_dict = item

        return bigger_dict 

    for i in range(limit):

        bigger_item_temp = bigger_item(data_temp)
        data_temp.remove(bigger_item_temp)

        price_bigger.append(bigger_item_temp)    

    return price_bigger

print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)

assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

print("The mission is done! Click 'Check Solution' to earn rewards!")
