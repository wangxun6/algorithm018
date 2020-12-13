学习笔记
本周主要学习了位运算，布隆过滤器，LRU算法以及排序算法。
（1）位运算：
 
异或操作去重 a ^ b ^ a = b可以实现去重操作
 n & (n-1)消去n最右边的1
判断整数的奇偶n&1==1 奇数 n&1==0 偶数
等等还有很多其他的操作，例如>>右移，<<左移
（2）布隆过滤器
本质上布隆过滤器( BloomFilter )是一种数据结构，比较巧妙的概率型数据结构（probabilistic data structure），特点是高效地插入和查询，可以用来告诉你 “某样东西一定不存在或者可能存在”。
相比于传统的 Set、Map 等数据结构，它更高效、占用空间更少，但是缺点是其返回的结果是概率性的，而不是确切的。
原理：布隆过滤器内部维护一个bitArray(位数组)， 开始所有数据全部置 0 。当一个元素过来时，能过多个哈希函数（hash1,hash2,hash3....）计算不同的在哈希值，并通过哈希值找到对应的bitArray下标处，将里面的值 0 置为 1 。 需要说明的是，布隆过滤器有一个误判率的概念，误判率越低，则数组越长，所占空间越大。误判率越高则数组越小，所占的空间越小。
布隆过滤器的核心思想有两点：
1.	多个hash，增大随机性，减少hash碰撞的概率
2.	扩大数组范围，使hash值均匀分布，进一步减少hash碰撞的概率。
虽然布隆过滤器已经尽可能的减小hash碰撞的概率了，但是，并不能彻底消除，因此正如上面的小例子所举的小例子的结果来看， 布隆过滤器只能告诉我们某样东西一定不存在以及它可能存在。
（3）LRU算法
LRU（Least recently used，最近最少使用）算法根据数据的历史访问记录来进行淘汰数据，其核心思想是“如果数据最近被访问过，那么将来被访问的几率也更高”。
思路：设计一个定长队列，如果数据被命中，则更新位置，不足时候，将最旧的数据进行丢弃。
（4）排序算法

冒泡排序python实现
def bubble_sort(items):
# 时间复杂度为O(n^2),排序是稳定的
    for i in range(len(items) - 1):
        for j in range(len(items)-1-i): 
            if items[j] > items[j+1]:
                items[j],items[j+1] = items[j+1],items[j]
        i += 1
    print("共循环%d次"%i)
    print(items)
    return items
选择排序python实现
def selection_sort(arr):
# 时间复杂度为O(n^2),排序是不稳定的
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index] ,arr[i] = arr[i],arr[min_index]
    print(arr)
    return  arr
插入排序
def insert_sort(arr):
# 时间复杂度O(n^2),排序是稳定的
    n = len(arr)
    for i in range(1,n):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                j -= 1
            else:
                break
    print(arr)
    return arr
希尔排序
def shell_sort(arr):
#     # 位运算
    # 希尔排序，就是分成多个间隔进行插入排序，随着间隔的缩小，最后形成有序数组
    # 时间复杂度最坏情况下为O(n^2),排序是不稳定的
    n = len(arr)
    gap = n >> 1
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j > 0:
                if arr[j] < arr[j-gap]:
                    arr[j-gap],arr[j] = arr[j],arr[j-gap]
                    j -= gap
                else:
                    break
        gap >>= 2
    print(arr)
    return arr
快排：
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index - 1, nums)
    quick_sort(pivot_index + 1, end, nums)


def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
归并排序
def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
堆排序
def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp


def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
此外还有计数排序、桶排序，基数排序等特殊排序。
