def sort_integers(numList):
    size = len(numList)
        
    for i in range(size - 1):
        for j in range(0, size-i-1):
            if numList [j] < numList[j+1]:
                numList[j], numList[j+1] = numList[j+1], numList[j]