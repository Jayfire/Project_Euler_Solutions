import math

def sumdiv(n):
    divs = 0

    for i in range(1,int(math.sqrt(n))):
        if n % i == 0:
            divs += i
            divs += n / i

    return divs

if __name__ == "__main__":

    
