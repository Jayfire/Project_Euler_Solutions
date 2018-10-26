

if __name__ == "__main__":
    bignum = str(2**1000)
    bigsum = 0

    for i in bignum:
        bigsum += int(i)

    print("The sum of the digits of 2^1000 is {}".format(bigsum))
