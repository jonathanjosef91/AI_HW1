

def giveNextEven():
    yield 0
    yield 2
    yield 4
    yield 6
    yield 8
    yield 10


for i in giveNextEven():
    print(i)

for i in giveNextEven():
    print(i)
