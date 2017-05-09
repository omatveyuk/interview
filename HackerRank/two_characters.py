"""Find max length of substring of string which satisfy the conditions: 
    Convert given string by deleting chars from string. 
    New string has to contain only two distinct characters and there are no more 
    than two consecutive char's present.

    Substring with two distinct characters are x and y, then substring could be 
    xyxyx or yxyxy but not xxyy or xyyx!!!!
  
   Example:
   Given string: beabeefeab
   The string contains: b, e, a, f 
   If we delete e, f the substring will be babab. Valid stirng with length 5
   If we delete a, g the substring will be bebeeeb. Not valid string because
   there are three consecutive e's present. So length of this string 0.
   If we delete only e, the resulting string is babfab. This is not a valid 
   string  because it contains three distinct characters. Length = 0
   Our answer is length = 5

   >>> two_chars('beabeefeab')
   5
   >>> two_chars('')
   0
   >>> two_chars('aaaaaaa')
   0
   >>> two_chars('uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon')
   0
"""

def two_chars(s):
    import re
    # create unque pair of chars of string
    unique_pair = set([])
    for i in xrange(0, len(s)-1):
        for j in xrange(i+1, len(s)):
            if s[i] != s[j]:
                if s[i] > s[j]:
                    unique_pair.add((s[j], s[i]))
                else:
                    unique_pair.add((s[i], s[j]))

    max_length = 0        
    for pair in unique_pair:
        regex_str = '[^'+pair[0]+pair[1]+']'
        new_str = re.sub(regex_str, '',s)
        if len(new_str) > max_length:
            valid_str = True
            for i in xrange(len(new_str)-1):
                if new_str[i] == new_str[i+1]:
                    valid_str = False
                    break
            if valid_str:
                max_length = len(new_str)

    print max_length

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T! ***\n"
        


