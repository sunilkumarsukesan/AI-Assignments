listone = list("Sunil")
listtwo = list("kumar")
listone.extend(listtwo)
print(listone)


def recursion(x):
    if x==0:
        return
    print(x)
    print(__name__)
    recursion(x-1)

if __name__ == "__main__":
    recursion(3)


sq = lambda num1 : num1 * num1
print(sq(3))

for _ in range(10):
    print("Test")


def returnNum():
    return 10,20

_, _ = returnNum()
print(_)
import math
print(math.__doc__)