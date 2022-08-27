def cardSort(a):
    for i in range (1, len(a)-1):
        inTeVoegenGetal = a[i] #x = in toe voegen element
        j = i #index tot waar array gesorteerd is
        while j > 0 and inTeVoegenGetal < a[j-1]: #tot j aan laatste element zit en het 
            a[j] = a[j-1]
            j = j-1
        a[j] = inTeVoegenGetal


arr = [44,55,12,42,94,18,6,67]
cardSort(arr)
print(len(arr))



