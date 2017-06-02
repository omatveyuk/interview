"""Given a word W, rearrange the letters of W to construct another word S in such
   a way that S is lexicographically greater than W. In case of multiple possible
   answers, find the lexicographically smallest one among them.

   >>> bigger_is_greater('ab')
   'ba'

   >>> bigger_is_greater('bb')
   'no answer'

   >>> bigger_is_greater('hefg')
   'hegf'

   >>> bigger_is_greater('dhck')
   'dhkc'

   >>> bigger_is_greater('dkhc')
   'hcdk'

"""

def bigger_is_greater(word):
    """Next lexicographical permutation algorithm."""
    word_lst = [char for char in word]
    length = len(word_lst)
    # 1. Find largest index i such that array[i-1] < array[i]
    #   (If no such i exists, then this is already the last permutation.)

    # print word_lst
    # print "Find largest index i such that array[i-1] < array[i]"
    index = None
    for i in xrange(1, length):
        if word_lst[i] > word_lst[i-1]:
            index = i
    # print 'i:', index
    if index is None:
        return "no answer"

    # print "Find largest index j such that j >= i and array[j] > array[i-1]"
    pivot = None
    # 2. Find largest index j such that j >= i and array[j] > array[i-1]
    for j in xrange(index, length):
        if word_lst[j] > word_lst[index-1]:
            pivot = j
    # print "j:", pivot

    # print "Swap array[j] and array[i-1]"
    # 3. Swap array[j] and array[i-1]
    word_lst[pivot], word_lst[index-1] = word_lst[index-1], word_lst[pivot]
    # print word_lst


    # print "Reverse the suffix starting at array[i]"
    # 4. Reverse the suffix starting at array[i]
    middle = (length - index) / 2
    # print "middle:", middle
    for i in xrange(middle):
        word_lst[index+i], word_lst[length-1-i] = word_lst[length-1-i], word_lst[index+i]
        # print word_lst

    return ''.join(word_lst)




if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print "********** All Tests are passed. *************"
