'''def LargeSmallSum(arr)
The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and second smallest from the odd position of given ‘arr’
Assumption:
All array elements are unique
Treat the 0th position as even
NOTE
Return 0 if array is empty
Return 0, if array length is 3 or less than 3
Example
Input
arr:3 2 1 7 5 4
Output
7
Explanation
Second largest among even position elements(1 3 5) is 3
Second smallest among odd position element is 4
Thus output is 3+4 = 7'''
arr=list(int(i) for i in input().split())
def LargeSmallSum(arr):
    length = len(arr)
    e = []
    o = []
    for i in range(length):
        if i % 2 == 0:
            e.append(arr[i])
        else:
            o.append(arr[i])
    even = sorted(e)
    odd = sorted(o)
    sum=even[-2]+odd[1]
    return sum
print(LargeSmallSum(arr))