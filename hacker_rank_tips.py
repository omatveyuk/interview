#!/bin/python

import sys

# if ome value in line
n = int(raw_input().strip())

#if two value in line and get them from list
n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]

# if n elements in line, read, create list, convert each value to int
c = map(int, raw_input().strip().split(' '))


# read lines from stdin (like lines from file)
for line in sys.stdin:


#try, except
S = raw_input().strip()
try:
    print int(S)
except ValueError:
    print "Bad String"








    # Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

dict_doctype = {}
set_applicationid = set([])

fl = False
for line in sys.stdin:
    if fl == True:
        filename, owner, docType, applicationId, contentLength = line.rstrip().split(',')
        if docType in dict_doctype.keys():
            dict_doctype[docType].add(applicationId)
        else:
            dict_doctype[docType] = set([applicationId])
        set_applicationid.add(applicationId)
    fl = True
    
sorted_key = sorted(dict_doctype.keys())
for key in sorted_key:
    print key

    diff = set_applicationid - dict_doctype[key]
    diff = sorted(list(diff))
    for item in diff:
        print item,      
    print
 