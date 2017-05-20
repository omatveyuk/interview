def semiprimeByNumber(n):
    import math
    def isPrime(number):
        if number == 2:
            return True
        for i in xrange(2, int(math.ceil(math.sqrt(number)))+1):
            if number % i == 0:
                return False
        return True

    def findDenomenators(number):
        return [n for n in xrange(2,number+1) if number % n == 0 ]

    def findPrimes(arr, primes):
        primes_from_arr = []
        for n in arr:
            if n in primes:
                primes_from_arr.append(n)
            elif isPrime(n):
                primes_from_arr.append(n)
                primes.add(n)
        return primes_from_arr
    
    count = 0
    number = 2
    primes = set([2])
    while count < n:
        denomenators = findDenomenators(number)
        print denomenators
        cur_primes = findPrimes(denomenators, primes)
        print cur_primes
        for i in xrange(len(cur_primes)):
            for j in xrange(i+1):
                if cur_primes[i]* cur_primes[j] == number:
                    count += 1
                    if count == n:
                        return cur_primes[i]* cur_primes[j]

        number += 1



    # semiprimes.sort()
    # return semiprimes[n-1]

print semiprimeByNumber(15)