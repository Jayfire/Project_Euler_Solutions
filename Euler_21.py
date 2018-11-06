import math

def sumdiv(n):
    divs = 0

    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            divs += i
            if i != 1:
                divs += n / i

    return divs

if __name__ == "__main__":

    amicable = set()
    maximum = int(input("Input the upper bound for the amicable numbers: "))

    for i in range(1,maximum):
        divi = sumdiv(i)
        for j in range(i+1,maximum):
            if divi == sumdiv(j):
                amicable.add(i)
                amicable.add(j)


    print("The sum of all amicable numbers under {} is {}".format(maximum, sum(amicable)))
