from msilib import MSIMODIFY_DELETE


def mergesort(a) -> None:
    mergeSortRecursive(a,0 ,len(a)-1)

def mergeSortRecursive(a,start,end):
    if start < end:
        middle = int((start+end)/2)
        mergeSortRecursive(a,start ,middle)
        mergeSortRecursive(a,middle+1 ,end)
        merge(a,start,middle,end)


def merge(a,start,middle,end):
    i = start #teller linkerrij
    j = middle+1 #teller rechter rij
    k = i #doorloop hulparray
    helpA = [None]*len(a)
    # vergelijken L en R deel en hulpA opvullen
    while i <= middle and j <= end:
        if a[i] <= a[j]:
            helpA[k] = a[i]
            i += 1
        else:
            helpA[k] = a[j]
            j += 1
        k +=1

    #elementer resterend in rechterDeel? plaats rest in hulpA
    if i > middle:
        while j <= end:
            helpA[k] = a[j]
            j += 1
    else:
        while i <= end:
            helpA[k] = a[i]
            i += 1
                         
    for i in range(start,end+1):
        a[i] = helpA[i]



arr = [44,66,11,3,7,99,5,44,3,22,15,6,8]
mergesort(arr)
print(arr)