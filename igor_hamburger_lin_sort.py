''' Python Linear Sort Exercise '''

#########################################
# Question 1 - do not delete this comment
#########################################
def countingSort(arr: list[int]) -> list[int]:
    '''
    Returns a sorted array of the input array using counting sort algorithm.
    '''

    if len(arr) < 1:
        return []
    max_num = max(arr)
    rang_lst = [0] * (max_num + 1)
    for num in arr:
        rang_lst[num] += 1
    sort_lst = []
    for i in range(len(rang_lst)):
        if len(sort_lst) == len(arr):
            return sort_lst
        while rang_lst[i] > 0:
            sort_lst.append(i)
            rang_lst[i] -= 1
    return sort_lst

    #sort_lst = [0] * len(arr)
    #for i in range(1, (max_num + 1)):
    #    rang_lst[i] += rang_lst[i - 1]

    #k = len(arr) - 1
    #while k >= 0:
    #    cur = arr[k]
    #    rang_lst[cur] -= 1
    #    new_position = rang_lst[cur]
    #    sort_lst[new_position] = cur
    #    k -= 1
    #    return sort_lst

#########################################
# Question 2 - do not delete this comment
#########################################
def radixSort(arr: list[int]) -> list[int]:
    '''
    Returns a sorted array of the input array using radix sort algorithm.
    '''

    if len(arr) < 1:
        return []
    max_num = max(arr)
    p = 1
    while max_num // p > 0:
        counting_sort2(arr, p)
        p *= 10
    return arr

def counting_sort2(arr, p):
    n = len(arr)
    sorted_lst = [0] * n
    count_lst = [0] * 10
    for i in range(n):
        indx = arr[i] // p
        count_lst[indx % 10] += 1
    for i in range(1, 10):
        count_lst[i] += count_lst[i - 1]

    k = n - 1
    while k >= 0:
        indx = arr[k] // p
        sorted_lst[count_lst[indx % 10] - 1] = arr[k]
        count_lst[indx % 10] -= 1
        k -= 1

    for i in range(n):
        arr[i] = sorted_lst[i]

#########################################
# Question 3 - do not delete this comment
#########################################
def bucketSort(arr: list[int]) -> list[int]:
    '''
    Returns a sorted array of the input array using bucket sort algorithm.
    '''

    if len(arr) < 1:
        return []
    min_num = min(arr)
    max_num = max(arr)
    buckets_lst = [[] for i in range(len(arr))]
    for num in arr:
        indx = lambda x: int((x - min_num)/(max_num - min_num)) * len(arr)
        if indx(num) >= len(arr):
            buckets_lst[len(buckets_lst)-1].append(num)
        elif indx(num) < 0:
            buckets_lst[0].append(num)
        else:
            buckets_lst[indx(num)].append(num)
    sorted_lst = []
    for s in buckets_lst:
        if len(s) > 0:
            selection_sort(s, len(s))
            sorted_lst += s
    return sorted_lst

def selection_sort(arr, size):
    if size <= 1:
        return arr
    elif size == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
        else:
            return arr
    for i in range(size):
        min_indx = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]

###################################
# Main - do not delete this comment
###################################
if __name__ == '__main__':
    # comment out the algorithms you don't want to run
    #sort_func = countingSort
    #sort_func = radixSort
    sort_func = bucketSort

    # test cases
    arr_list = [
        [12, 11, 13, 5, 11, 6, 7],
        [],
        [24, 4, 140, 67, 102, 45],
        [120, 200, 300, 500, 10],
        [-1, 2, -5, 10, 11, 0],
        [1.2, 2.3, 0.2, 2.1, 2.09]
    ]

    for arr in arr_list:
        print('Before sorting: {}'.format(arr))
        sorted = sort_func(arr)
        print('After sorting: {}'.format(sorted))
        print()