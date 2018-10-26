import math

if __name__ == "__main__":
    A = .0203000500000007
    n = 10001
    power = 2**n
    pop = 10**power
    popn = pop / n
    one = math.floor(pop * A)
    two = (popn * A)
    three = math.floor(popn * A)

    print(int(one - two * three))
