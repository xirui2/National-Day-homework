def find(n,array):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left+right)//2
        if n == array[mid]:
            print(n)
            return True
        if n > array[mid]:
            left = mid + 1
        if n < array[mid]:
            right = mid -1  
    return False
    
array = range(0,1000000)
flag = find(45,array)
print(flag)
