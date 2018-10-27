from math import factorial


if __name__ == "__main__":
    onehundred = factorial(100)
    onehundred = str(onehundred)
    summed = 0
    for x in onehundred:
        summed += int(x)
    print(summed)
