def format_ingredients(items):

    if items:

        ingredients = items[0]

        for i in range(1, len(items)-1):
            ingredients += ", " + items[i]
        
        if len(items) == 1:
            return ingredients
        else:
            return f"{ingredients} and {items[len(items)-1]}"
    else:
        return ""
            