def nonDivisibleSubset(k,arrayOfNumbers): # k is the divisor and arrayOfNumbers contains 
                                            #all the elements in an array.
    elementsArray=[]
    for i in range(k):
        elementsArray.append(0)
    for i in arrayOfNumbers:
        elementsArray[i%k]+=1   # Through the iteration of this loop, we get the count of elements
                                    #for the possible reaminders.
    maxSubsetCount=min(elementsArray[0],1)
    for i in range(1,k//2+1):
        if i==k-i:
            maxSubsetCount+=1
        else:
            maxSubsetCount+=max(elementsArray[i],elementsArray[k-i])
    return maxSubsetCount
print(nonDivisibleSubset(4,[19,12,10,22,24,25,10]))