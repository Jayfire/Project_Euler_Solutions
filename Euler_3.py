def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            if d not in factors:
                factors.append(d)
            n /= d
        d = d + 1

    return factors


pfs = prime_factors(600851475143)
print(max(pfs))