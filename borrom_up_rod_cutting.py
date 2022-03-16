import time

INT_MIN = -30000
 
# Returns the best obtainable price for a rod of length n and price[] as prices of different pieces
def cutRod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
 
    # Build the table val[] in bottom up manner and return  the last entry from the table
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
 
    return val[n]
 
# Driver program to test above functions
arr = []
size = int(input("Please choose the size: "))
for i in range(0, size):
    elements = int(input())
    arr.append(elements) # adding the element

start = time.time()
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))
finish = time.time()
print("Run Time: %fs"%(finish - start))