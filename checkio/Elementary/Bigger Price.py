def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    """
    TOP most expensive goods
    """
    # your code here
    
    data_temp = data.copy()    

    def bigger_item(data: list[dict]):
        bigger_list = {}
        price = 0

        for item in data:

            if price < item["price"]:
                price = item["price"]
                bigger_list = item

        return bigger_list 

    bigger_item1 = bigger_item(data_temp)
    

    return []


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
