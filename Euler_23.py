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

    abundant = set()
    formable = set()
    summed = 0
    maximum = 28123

    for i in range(12,maximum):
        divi = sumdiv(i)
        if divi > i:
            abundant.add(i)

    for i in abundant:
        for j in abundant:
            formable.add(i+j)

    for i in range(28123):
        if i not in formable:
            summed += i


    print("The sum of all numbers that are not the sum of two abundant numbers is {}".format(summed))
