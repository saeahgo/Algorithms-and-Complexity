'''
    In regards with quicksort, it is possible to select any element for pivot
    since, selecting ending element is common. Ending element is selected as pivot
'''
#import time # for time.time() function
import timeit

def partition(arr,start,end):
    i = start # selecting i as the first element of the arr (start)
    pivot = arr[end]
    
    for j in range(start,end):
        '''
            if arr[j] <= pivot element then swapping takes place to ensure that after this for loop all the elements
            smaller than pivot are to its left side (ignoring the order)
        '''
        if arr[j] <= pivot:
            # for swapping using temp
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i+1

    # swapping without temp so that the pivot element is at its true position
    arr[i], arr[end] = arr[end],arr[i]
    return i

def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)


# creating an empty list
arr = []
# number of elements as input
n = int(input("Enter number of elements : "))
#start_time = time.time() # measuring the start time before sorting
# iterating till the range
for i in range(0, n):
    elements = input()
    arr.append(elements) # adding the element

#arr= [2,8,5,3,9,4,1,7]
#arr = [E,X,A,M,P,L,E]
#arr = [t,a,b,l,e,s]
#arr = [1,8,4,9,3]

#start_time = time.time() # measuring the start time before sorting
start_time = timeit.default_timer()
print("The array before sorting is: ", arr)
quick_sort(arr,0,len(arr)-1)
#end_time = time.time() # measuring the end time after sorting
#print(start_time, end_time)
end_time = timeit.default_timer()

print("The sorted array is: ", arr)
print("The execution time is: ", end_time - start_time)