def selection_sort_vooran(a):
    n = len(a)
    for i in range(0,n-1):
        positie = i
        min = a[i]
        for j in range(i+1, n):
            if a[j] < min:
                positie = j
                min = a[j]
        a[positie] = a[i]
        a[i] = min


a = [54,5964,51,6,79,7,54,654]
selection_sort_vooran(a)
print(a)