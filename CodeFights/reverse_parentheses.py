""" Reverse substring inside parenthesis.
    A string s consists of English letters, punctuation marks, whitespace chars,
    and brackets. It is guaranteed that the parentheses in s form a regular 
    bracket sequence (number opened and closed brackets is equal).
    Your task is to reverse the strings contained in each pair of matching parentheses, 
    starting from the innermost pair. 
    The results string should not contain any parentheses.

    >>> reverseParentheses("a(bc)de")
    'acbde'

    >>> reverseParentheses("a(bcdefghijkl(mno)p)q")
    'apmnolkjihgfedcbq'


    >>> reverseParentheses("co(de(fight)s)")
    'cosfighted'

    >>> reverseParentheses("Code(Cha(lle)nge)")
    'CodeegnlleahC'

    >>> reverseParentheses("Where are the parentheses?")
    'Where are the parentheses?'

    >>> reverseParentheses("abc(cba)ab(bac)c")
    'abcabcabcabc'

    >>> reverseParentheses("The ((quick (brown) (fox) jumps over the lazy) dog)")
    'The god quick nworb xof jumps over the lazy'

"""

def reverseParentheses(s):
    new_s = ''
    temp = []
    stack = []
    for char in s:

        if stack == [] and char != '(':
            new_s += char

        elif char == ')':
            while stack != []:
                if stack[-1] == '(':
                    break
                temp.append(stack.pop())
            stack.pop()         # '('
            if stack != []:
                stack += temp
            else:
                new_s += ''.join(temp)
            temp = []

        else:
            stack.append(char)

    return new_s

if __name__ == "__main__":
    debug = True
    if debug:
        from doctest import testmod
        if testmod().failed == 0:
            print "********** All Tests are passed. *************"


