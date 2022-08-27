def bubble_sort(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp

a = [684, 654, 354,3854,89674,63854,354]
bubble_sort(a)
print(a)