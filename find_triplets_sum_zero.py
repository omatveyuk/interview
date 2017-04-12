"""Find all triplets with zero sum.
    Given an array of distinct elements. 
    The task is to find triplets in array whose sum is zero.

    >>> findTripletsSumZero([-1, 0, -3, 4, 1])
    [[-1, 0, 1], [-1, -3, 4]]

    >>> findTripletsSumZero([-1, 0, -3])
    []
"""

def findTripletsSumZero(numbers):
    """Find all triplets with zero sum."""

    # MY SOLUTION runtime: O(n^2) space: O(n)
    positive = [number for number in numbers if number > 0]
    negative = [number for number in numbers if number < 0]
    zero = [number for number in numbers if number == 0]

    if positive == [] or negative == []:
        return []

    result = []
    if zero != []:
        for number in positive:
            if -number in negative:
                result.append([-number, 0, number])

    negative = dict.fromkeys(negative, 0)
    for i in xrange(len(positive)-1):
        for j in xrange(i+1, len(positive)):
            if -(positive[i]+positive[j]) in negative:
                result.append([-(positive[i] + positive[j]), positive[i], positive[j]])

    negative = negative.keys()
    positive = dict.fromkeys(positive, 0)
    for i in xrange(len(negative)-1):
        for j in xrange(i+1, len(negative)):
            if -(negative[i]+negative[j]) in positive:
                result.append([negative[j], negative[i], -(negative[i] +negative[j])])

    # SOLUTION #2 native runtime: O(n^3)  space: O(1)
    # result = []
    # for i in xrange(len(numbers ) - 2):
    #     for j in xrange(i+1, len(numbers) - 1):
    #         for k in xrange(j+1, len(numbers)):
    #             if numbers[i] + numbers[j] + numbers[k] == 0:
    #                 result.append([numbers[i], numbers[j], numbers[k]])

    # SOLUTION #3 using hashtable runtime: O(n^2) space: O(n)
    # Pseudo-code:
    # Run a loop from i=0 to n-2
    #   Create an empty hash table
    #   Run inner loop from j=i+1 to n-1
    #     If -(arr[i] + arr[j]) is present in hash table
    #        print arr[i], arr[j] and -(arr[i]+arr[j])
    #     Else
    #        Insert arr[j] in hash table.
    # result = []
    # for i in xrange(len(numbers)-1):
    #     dict_temp = {}
    #     for j in xrange(i+1, len(numbers)):
    #         if -(numbers[i] + numbers[j]) in dict_temp:
    #             result.append([-(numbers[i] + numbers[j]), numbers[i], numbers[j]]) 
    #         else:
    #             dict_temp[numbers[j]] = ''

    # SOLUTION #4 using sort runtime: O(n^2)  scpace:O(1)
    # Pseudo-code:
    # Sort all element of array
    # Run loop from i=0 to n-2.
    #     Initialize two index variables l=i+1 and r=n-1
    #     While (l < r) 
    #         Check sum of arr[i], arr[l], arr[r] is zero or not if sum is zero then 
    #         append the triplet to the result and do l++ and r--.
    #     
    #         If sum is less than zero then l++
    #         If sum is greater than zero then r--
    # result = []
    # numbers.sort()
    # for i in xrange(len(numbers) - 1):
    #     l = i + 1
    #     r = len(numbers) - 1
    #     while l < r:
    #         sum_zero = numbers[i] + numbers[l] + numbers[r]
    #         if sum_zero == 0:
    #             result.append([numbers[i], numbers[l], numbers[r]])
    #             l += 1
    #             r -= 1
    #         elif sum_zero < 0:
    #             l += 1
    #         else:
    #             r -= 1 



 

    return result

if __name__ == '__main__':
    import doctest

    print
    if doctest.testmod().failed == 0:
        print "\t*** ALL TESTS PASSED; GOOD WORK! ***"
    print
