def quicksort1(array):
    if len(array) < 2:
        # return array
        print(array)

def quicksort2(array):
    if len(array) == 2:
        if array[0] > array[1]:
            array = array[::-1]
            print(array[::-1])
            # return array
        else:
            print(array)
            # return array
'''
def quicksort(array):
    if len(array) > 2:
        pivot = array[0]
        s_pivot = []
        g_pivot = []
        for i in range(1, len(array)):
            if array[i] <= pivot:
                s_pivot += array[i]
            else:
                g_pivot += array[i]
        print(s_pivot+pivot+g_pivot)
'''

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i >= pivot]
        return quicksort(less)+[pivot]+quicksort(greater)


a = [5]
quicksort1(a)
b= [16,9]
quicksort2(b)
c = [9,16,5,89,7,14,23,2,30,5,9]
print(quicksort(c))

'''
quicksort FUNCTION IS GIVING AN ERROR. INT OBJECT IS NOT ITERABLE AT LINE 23.
AS I THINK I AM TOO DUMB TO UNDERSTAND THIS ERROR, I WILL REALLY LIKE TO GET UNDEERSTOOD(Edit: I understood:)).!
'''
