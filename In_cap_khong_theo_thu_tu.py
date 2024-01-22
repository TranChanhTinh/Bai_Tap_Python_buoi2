def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

arrayA =[1,2,4,5,6]
arrayB =[2,5,7,8,9]
printUnorderedPairs(arrayA, arrayB)