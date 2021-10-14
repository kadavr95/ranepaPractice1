import random


def gen_list(n):
    customList = []
    gen = (random.randint(0, 10) for _ in range(n))
    for i in gen:
        customList.append(i)
    return customList


def check_element(list, element):
    for i, listEl in enumerate(list):
        if listEl == element:
            return i
    return None


print("Enter searched value and length of the list")
element = int(input())
length = int(input())
customList = gen_list(length)
print("list:", customList)
checkResult = check_element(customList, element)
if checkResult:
    print("position:", checkResult)
else:
    print("not found")
    sum = 0
    for i, listEl in enumerate(customList):
        if i % 2 == 0:
            sum += listEl
    print("sum:", sum)
