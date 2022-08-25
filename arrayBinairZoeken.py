#p6 Algoritme 1.2 Binair zoeken in een array geïmplementeerd m.b.v. iteratie
def binarySearch(target, sortedArray):
    l = 0
    r = len(sortedArray) -1
    while l != r :
        m = int((l+r)/2)
        if sortedArray[m] < target:
            l = m +1
        else:
            r = m

    if sortedArray[l] == target:
        foundIndex = l
    else:
        foundIndex = -1

    return foundIndex

#with recursion
def binarySearchRecursive(target, sortedArray):
    return recursion(target, sortedArray, 0, len(sortedArray) -1)

def recursion(target, sortedArray, l, r):
    if l == r:
        if target == sortedArray[l]:
            return l
        else:
            return -1

    else:
        m = int((l+r)/2)
        if sortedArray[m] < target :
            return recursion(target, sortedArray, m+1, r)
        else:
            return recursion(target, sortedArray, l, m)


print(binarySearchRecursive(2, [0,1,1,1,1,2,3,4,5,6]))