FIBLIST = [None]*4000000

def fib(x):
    if FIBLIST[x]:
        return FIBLIST[x]

    FIBLIST[x] = fib(x-1) + fib(x-2)
    return FIBLIST[x]

if __name__ == "__main__":
    total = 0
    FIBLIST[0], FIBLIST[1] = 1, 1
    for x in range(2,4000000,2):
        total += fib(x)

    print(total)
