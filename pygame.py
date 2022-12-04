def miniMaxSum(arr):
    # Write your code here
    arrmax = copy(arr)
    arrmin = copy(arr)
    arrmax.remove(min(arrmax))
    print(arrmax)
    arrmin.remove(max(arrmin))
    print(arrmin)
    mini = sum(arrmin)
    maxi = sum(arrmax)
    print(mini,' ',maxi)


print(miniMaxSum([1,2,3,4,5]))
