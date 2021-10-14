import random


def gen_list(n):
    customList = []
    for i in range(0, n):
        customList.append(random.randint(0, 100))
    return customList


print("Enter length of the list")
listLength = int(input())
customList = gen_list(listLength)
print("list:", customList)
for i in range(0, listLength):
    customList[i] **= 2
print("list:", customList)
