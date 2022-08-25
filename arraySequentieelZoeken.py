#p3 Algoritme 1.1 Sequentieel zoeken in een array
def seqSearch(item, list):
    #set index
    i = 0
    #stop when index passed last item of list
    #or when item found at index
    while (i < len(list) and list[i]!= item):
        #not found -> move index 1 position
        i += 1
    
    #index didn't pass last item of list? index found, return it
    #else notfound, retourn -1
    if i < len(list):
        index = i
    else:
        index = -1

    return index


print(seqSearch(4, [1,2,3,4,5,6,7]))
