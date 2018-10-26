def collatzcount(n):
    original = n
    steps = 0

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3*n + 1) // 2
        steps += 1

    return (original, steps)

if __name__ == "__main__":
    steps = [0,0]

    for i in range(1000000):
        tempsteps = collatzcount(i)

        if tempsteps[1] > steps[1]:
            steps[0] = tempsteps[0]
            steps[1] = tempsteps[1]

    print("Number with longest chain: {}\nLongest chain count: {}".format(steps[0], steps[1]))
