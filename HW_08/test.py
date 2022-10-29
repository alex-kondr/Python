import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

for cat in Cat:
    print(cat[0])