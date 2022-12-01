import random

participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}

def get_random_winners(quantity, participants):

    users_list = [key for key in participants]

    # print(users_list)

    random.shuffle(users_list)
    # print(users_list)

    if quantity > len(users_list):
        return []

    else:
        return random.sample(users_list, quantity)


print(get_random_winners(3, participants))



