def checkio(words: str) -> bool:
    # add your code here
    word_list = words.split(" ")
    count = 0

    for word in word_list:

        if word.isalpha():
            count += 1

            if count == 3:
                return True
        
        else:
            count = 0

    return False


print("Example:")
print(checkio("Hello World hello"))

assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
