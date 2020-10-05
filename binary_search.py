import math

# Binary Search Algorithm
search_list = [1, 20, 4, 5, 49, 492, 58, 50, 20, 56, 48, 2, 48, 70]

search_list.sort()
iter_count = 0
target = 492

while True:
    mid = search_list[math.floor(len(search_list) / 2)]

    if mid > target:
        search_list = search_list[0 : search_list.index(mid) + 1]
    elif mid < target:
        search_list = search_list[search_list.index(mid) : len(search_list) + 1]

    iter_count += 1

    if mid == target:
        break

print(target, mid, iter_count)
