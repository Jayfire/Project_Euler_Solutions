def fib(x):
    if x == 0 or x == 1:
        return 1
    return fib(x-1) + fib(x-2)
total = 0
for x in range(3,4000000,3):  
    total += fib(x)
print(temp)