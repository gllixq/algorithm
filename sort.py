#-*- coding:utf-8 -*-
#  冒泡排序
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        print li


# 选择排序
def select_sort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[min_index] > li[j]:
                min_index = j
        li[min_index], li[i] = li[i], li[min_index]


# 插入排序
def insert_sort(li):
    if len(li) == 1:
        return
    for i in range(0, len(li) - 1):
        j = i + 1
        while j > 0:
            if li[j] < li[j - 1]:
                li[j], li[j - 1] = li[j - 1], li[j]
                j = j - 1
            else:
                break


# 快速排序
def partion(li, left, right):
    temp_val = li[left]
    while left < right:
        while right > left and li[right] >= temp_val:
            right = right - 1
        li[left] = li[right]
        while left < right and li[left] <= temp_val:
            left = left + 1
        li[right] = li[left]
    li[left] = temp_val
    return left

    return -1


def quick_sort(li, left, right):
    if left < right:
        mid = partion(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [8, 9, 7, 6, 5, 4, 3, 2, 1]
quick_sort(li, 0, len(li) - 1)
print li