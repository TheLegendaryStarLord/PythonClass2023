def calc_mean(numList):
    sumValue = 0
    for x in numList:
        sumValue += x
    mean = sumValue / len(numList)
    display = str(mean)
    return display

def calc_median(numList):
    size = len(numList)
    
    for i in range(size - 1):
        for j in range(0, size - i - 1):
            if numList[j] < numList[j + 1]:
                numList[j], numList[j + 1] = numList[j + 1], numList[j]
                
    
    if size % 2 == 1:
        median = numList[size // 2]
    else:
        median = (numList[size // 2 - 1] + numList[size // 2]) / 2
    
    
        
    display = str(median)
    return display