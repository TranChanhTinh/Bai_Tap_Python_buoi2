def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i + 1,len(array)):
            print(str(array[i]) + "," + str(array[j]))

array=[1,5,7,8,9,]
printUnorderedPairs(array)