def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        print li


def select_sort(li):
    for i in range(len(li)):
        min_val = li[i]
        min_index = i
        for j in range(i + 1, len(li) - i):
            if min_val > li[j]:
                min_val = li[j]
                min_index = j
        li[min_index] = li[i]
        li[i] = min_val


li = [9, 8, 7, 6, 5, 4, 3, 2, 1]
select_sort(li)
print li