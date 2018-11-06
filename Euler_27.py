import math

PRIMES = [None]*100000

def isprime(n):
    if n <= 0: return False

    if PRIMES[n] != None:
        return PRIMES[n]

    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            PRIMES[n] = False
            return PRIMES[n]

    PRIMES[n] = True
    return PRIMES[n]

def primelen(a,b):
    n = 0
    total = 0


    while True:
        num = n**2 + a*n + b
        if not isprime(num):
            break

        total += 1
        n += 1

    return total

if __name__ == "__main__":

    primeamount = 0
    coef = [0,0]

    for a in range(-999,1000):
        for b in range(-999,1001):
            currlen = primelen(a,b)
            if currlen > primeamount:
                coef[0], coef[1] = a, b
                primeamount = currlen

    print("a: {}, b: {}, product: {}".format(coef[0], coef[1], coef[0]*coef[1]))
