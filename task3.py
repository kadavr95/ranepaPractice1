import random


def gen_list(n):
    customList = []
    gen = (random.randint(0, 100) for _ in range(n))
    for i in gen:
        customList.append(i)
    return customList


print("Enter dimensions for the two lists (one on each line)")
length_a = int(input())
length_b = int(input())
list_a = gen_list(length_a)
print("list 1:", list_a)
list_b = gen_list(length_b)
print("list 2:", list_b)
tuple_c = tuple(list_a + list_b)
print("tuple:", tuple_c)
sum = 0
for i in range(0, int((length_a + length_b) / 2)):
    sum += tuple_c[2 * i + 1]
print("sum:", sum)
