'''

Description:
练习堆排序的实现。（最大堆）
堆排序和快排都是不稳定的。

'''

def max_heapify(list_to_sort, i, length): # 注意这里最好放一个length参数，因为heap_sort的时候length是会变的
    left = 2*i+1
    right = 2*i+2
    larger = i
    if (left<length and list_to_sort[left]>list_to_sort[i]):
        larger = left
    if (right<length and list_to_sort[right]>list_to_sort[larger]):
        larger = right
    if (larger != i):
        list_to_sort[i], list_to_sort[larger] = list_to_sort[larger], list_to_sort[i]
        max_heapify(list_to_sort, larger,length)


def build_max_heap(list_to_sort):
    length = len(list_to_sort)
    for i in range(length//2, -1,-1):
        max_heapify(list_to_sort, i, length)


def heap_sort(list_to_sort):
    build_max_heap(list_to_sort)
    for i in range(len(list_to_sort)-1,0,-1):
        list_to_sort[i], list_to_sort[0] = list_to_sort[0], list_to_sort[i]
        length = i
        max_heapify(list_to_sort,0,length)






if __name__ == '__main__':
    array1 = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
    # array1 = [7,3,5,6,2,4,1]
    heap_sort(array1)
    print (array1)
    # quick_sort1(array1,0,len(array1)-1)
    # print array1
