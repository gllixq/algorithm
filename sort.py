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


# 堆排序(非递归实现)
# 自顶向下调整函数
def shif(li, node_index, max_index):
    temp_val = li[node_index] # 需要调整的根节点
    left_child_index = 2 * node_index + 1
    while left_child_index <= max_index:
        cur_max_index = left_child_index
        if left_child_index + 1 <= max_index and li[left_child_index] < li[left_child_index + 1]:
            cur_max_index = left_child_index + 1
        if li[cur_max_index] > temp_val:
            li[node_index], li[cur_max_index] = li[cur_max_index], li[node_index]
            node_index = left_child_index
            left_child_index = 2 * left_child_index + 1
        else:
            break


def shif_digui(li, low, high):
    temp_val = li[low]
    left_child_index = 2 * low + 1
    right_child_index = 2 * low + 2
    if left_child_index > high:
        return
    max_index = left_child_index
    if right_child_index <= high and li[right_child_index] > li[left_child_index]:
        max_index = right_child_index
    if temp_val < li[max_index]:
        li[low], li[max_index] = li[max_index], li[low]
        shif_digui(li, max_index, high)


def heap_sort(li):
    # 构造大根堆
    end_parent_inex = (len(li) - 2) // 2 # 最后一个根节点的index,先从最底部调整，保证调整过后的子二叉树都符合大根堆的性质
    for i in range(end_parent_inex, -1, -1):
        shif_digui(li, i, len(li) - 1)

    # 交换堆顶元素和最后一个叶子节点，然后对剩余元素进行堆构造
    for i in range(len(li) - 1, 0, -1):
        li[0], li[i] = li[i], li[0]
        shif_digui(li, 0, i - 1)


li = [8, 9, 7, 6, 5, 4, 3, 2, 1]
heap_sort(li)
print li