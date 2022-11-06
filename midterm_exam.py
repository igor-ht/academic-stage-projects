#1.1 question
def three_largest(lst):
#Solution by Ilya using three variable and one loop only, instead of my solution with a for and a while loop
    a, b, c = 0, 0, 0
    for num in lst:
        if num > a:
            a, b, c = num, a, b
        elif num > b:
            a, b, c = a, num, b
        elif num > c:
            a, b, c = a, b, num

    big_tupl = (a, b, c)

    return big_tupl

    # Time analysing O(n) => I used the bubble sort in a while loop so I can get the 3 biggest values of the list at the end of the same list    #c = 1
    #while c < 4:
    #    for m in range(len(lst)-c):
    #        if lst[m] > lst[m+1]:
    #            lst[m], lst[m+1] = lst[m+1], lst[m]
    #    c += 1
    #return tuple(lst[-3:])

#l = [99999, 9999, 5, 7, 0, 9, 8, 299, 9999999999, 99999999, 111111111]
#print(three_largest(l))

#1.2 question
def is_contained(lst1, lst2):

    if len(lst1) <= len(lst2):
        while len(lst1) > 0:
            for i in range(len(lst2)):
                if lst1[0] == lst2[i]:
                    return is_contained(lst1[1:], lst2[i+1:])
        return True
    return False

#lst1 = [0, 2, 3]
#lst2 = [0, 3, 0, 2, 3]
#print(is_contained(lst1, lst2))


#1.3 question
def most_appearences(dict):

    values_set = set(dict.values())
    the_number = 0

    for n in values_set:
        count = 0
        most_count = 0
        for j in values_set:
            if n == j:
                count += 1
        if count > most_count:
            most_count = count
            the_number = n

    return the_number

#dict = {'c': 2, 'a': 2, 'b': 1, 'f': 3, 'd': 3, 'e': 2, 'g': 3, 'h': 3}
#print(most_appearences(dict))

#(2) question
def basa_baggage(weights, w):

    if len(weights) == 0 or min(weights) > w:
        return 0
    else:
        weights.remove(min(weights))
        return 1 + basa_baggage(weights, w - (min(weights)))


    #weights.sort()
    #counter = 0
    #for i in range(len(weights)):
    #    if weights[i] > w:
    #       return counter
    #    elif weights[i] <= w:
    #       w -= weights[i]
    #       counter += 1
    #return counter

#print(basa_baggage([4,1,1,3],7))


#3 question
def my_mistery(a):
    p = len(a)//2
    a[0], a[p] = a[p], a[0]
    j = 0
    for i in range(1, len(a)):
        if a[i] < a[0]:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[0], a[j] = a[j], a[0]
    #return a
    #Big O is O(n) - linear
#print(my_mistery([10, 40, 20, 50, 60]))

#4 question
#4.1
def sort_up(lst):

    if len(lst) == 0:
        return []
    for i in range(1, len(lst)):
        if lst[0] > lst[i]:
            lst[0], lst[i] = lst[i], lst[0]
    return [lst[0]] + sort_up(lst[1:])

#print(sort_up([1,2,3,7,6,5,8,1]))

def quicksort_up(lst):
    if len(lst) > 1:
        piv = int(len(lst) / 2)
        val = lst[piv]
        left = [n for n in lst if n < val]
        right = [n for n in lst if n > val]
        middle = [n for n in lst if n == val]
        return quicksort_up(left) + middle + quicksort_up(right)
    else:
        return lst

#print(quicksort_up([1,2,3,7,6,5,8,1]))

#4.2
def sort_down(lst):

    if len(lst) == 0:
        return []
    for i in range(1, len(lst)):
        if lst[0] < lst[i]:
            lst[0], lst[i] = lst[i], lst[0]
    return [lst[0]] + sort_down(lst[1:])


#EXTRA FUNCTION 4FUN
def sort_up_test(lst1, lst2): #Function that returns one sorted list from two sorted lists

    lst1.append(float('inf'))
    lst2.append(float('inf'))
    if len(lst1) == 1 and len(lst2) == 1:
        return []
    if lst1[0] < lst2[0]:
        return [lst1[0]] + sort_up_test(lst1[1:len(lst1)-1], lst2[:len(lst2)-1])
    else:
        return [lst2[0]] + sort_up_test(lst1[:len(lst1)-1], lst2[1:len(lst2)-1])

#lst = [1,2,3,7,6,5,8,1]
#x = sort_up_test(sort_up(lst[(len(lst) // 2): len(lst)]), sort_up(lst[0: (len(lst) // 2)]))
#print(x)


#5 question
def get_max(lst1, lst2, k): #Big O of the function get_max => O(1) - constant

    if k > len(lst1)+len(lst2):
        raise ValueError (f'k needs to bem smaller than the lenght of both lists together')

    if lst1[0] < lst2[0]:
        if len(lst1) >= k:
            return lst1[k-1]
        else:
            return lst2[k - len(lst1)]
    else:
        if len(lst2) >= k:
            return lst2[k-1]
        else:
            return lst1[k - len(lst1)]

#print(get_max([3,12,13,14,15], [0,6,7,8], 6))


#EXTRAS
def merge_sort(lst):

    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
                k += 1
            else:
                lst[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst

#print(merge_sort([1,2,5,4, 5, 2, 1, 9, 10, 99, 3,4,1]))