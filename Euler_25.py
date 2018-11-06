FIBLIST = [None]*4000000

def fib(x):
    if FIBLIST[x]:
        return FIBLIST[x]

    FIBLIST[x] = fib(x-1) + fib(x-2)
    return FIBLIST[x]

if __name__ == "__main__":

    FIBLIST[0], FIBLIST[1] = 1, 1
    for x in range(5000):
        if len(str(fib(x))) == 1000:
            print("The first number to conatin 1000 digits is the {} indexed fibonacci number".format(x))
            break
