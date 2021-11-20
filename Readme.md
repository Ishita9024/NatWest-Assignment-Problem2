# Problem Statement
## Non Divisible Subset
In this problem an array with n number of values is given, we need to find the subset with the elements in which the sum of the any two numbers is not evenly divisible by the given number.
## Problem Solution
To solve this problem I have used a technique to find the remainder of each element and increment the count based on the condition.
- At first I have intialized an array and pushed all the possible remainder of the numbers given in an array.
```Python3
maxSubsetCount=min(elementsArray[0],1)
<!-- This will give the minimum of the array element. -->
```
- Then I am looping through the elements to get the number of iterations.

```python3
for i in range(1,k//2+1):
        if i==k-i:
```
- Then,we are comparing the values of the subsets and get the subset with maximum length of the elements.
- At the end I am returning the length of the subset with the sum of pairs of its elements that are not evenly divisible by the given number.
- The divisor and the array is passed as an argument.
