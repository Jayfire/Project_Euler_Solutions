if __name__ == "__main__":
    pal = []

    for x in range(900,1000):
        for y in range(900,1000):
            if str(x*y) == str(x*y)[::-1]:
                pal.append(x*y)

    print(max(pal))
