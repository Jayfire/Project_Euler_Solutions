n = 2520
div = list(range(1,21))
b = True
while b:
    counter = 0
    for x in div:
        if n % x == 0:
            counter += 1
    if counter == 20:
        print(n)
        b = not b
    n += 10