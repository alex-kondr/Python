from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here

    for i in range(len(elements)):
        
        if elements[i-1] != elements[i]:
            return False

    return True


print("Example:")
print(all_the_same([1, 1, 1]))

assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([2, 1, 1, 1]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
