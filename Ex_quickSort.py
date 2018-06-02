'''

Description:
练习快排的实现。

'''



def quickSort(list_to_sort, i, j):
    x = list_to_sort[i]
    low = i
    high = j
    if (low >= high):
        return
    while(low < high):
        while (list_to_sort[high] < x and low < high):
            high = high - 1
        # if (low < high):
        list_to_sort[low] = list_to_sort[high]
            # print (list_to_sort)

        while (list_to_sort[low] > x and low < high):
            low = low + 1
        # if (low < high):
        list_to_sort[high] = list_to_sort[low]
            # print (list_to_sort)
    # print (low)
    # print (high)
    list_to_sort[low] = x

    quickSort(list_to_sort, i, low-1)
    quickSort(list_to_sort, low+1, j)






if __name__ == '__main__':
    array1 = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
    # array1 = [7,3,5,6,2,4,1]
    quickSort(array1, 0, len(array1)-1)
    print (array1)
    # quick_sort1(array1,0,len(array1)-1)
    # print array1
