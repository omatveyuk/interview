"""Dynamic Array.
    n is number of sequence 
    q is number of query sequences S0={} S1={} S2={} . . . Sn={}
    Print last answer. 

    Input:
    Query type 1: 1 x y 
        Find index of sequence id = (x ^ lastAns) % n
        Append y in Sid-th sequence

    Query type 2: 2 x y 
        Find index of sequence id = (x ^ lastAns) % n
        Put in last answer value at (y%(size of Si-th sequence))
        Print last ansswer

    Example:
    n = 2 (two sequence), q = 5 (five queries)
    1 0 5       S[0] = [5]      last_ans = 0
    1 1 7       S[1] = [7]      last_ans = 0
    1 0 3       S[0] = [7, 3]   last_ans = 0
    2 1 0       S[1][0]: 7      last_ans = 7
    2 1 1       S[1][1]: 3      last_ans = 3


"""
try:
    with open('dynamic_array_input.txt') as f:
        n,q = f.readline().strip().split(' ')
        n,q = int(n),int(q)
        last_ans = 0
        seq = {}

        print "Number of sequence:",n
        print "Number of queries:", q

        for line in f:
            query, x, y = line.strip().split(' ')
            query, x, y = int(query), int(x), int(y)
            id_seq = (x ^ last_ans) % n
            if query == 1:
                if id_seq in seq:
                    seq[id_seq].append(y)
                else:
                    seq[id_seq] = [y]
                # print "1.", id_seq,":", seq[id_seq], "last ans:", last_ans
            elif query == 2:
                if id_seq in seq:
                    last_ans = seq[id_seq][y % len(seq[id_seq])]
                    # print "2.", id_seq, ":", seq[id_seq], "last ans:", last_ans
                print last_ans
except:
    print "The input file does not exist"
