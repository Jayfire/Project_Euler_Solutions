

def charpos(c):
    return ord(c) - 96

if __name__ == "__main__":
    f = open("names.txt","r")

    names = []

    for line in f:
        names = line.replace("\"","").split(",")

    names = sorted(names)

    bigsum = 0

    for i in range(len(names)):
        tinysum = 0

        for char in names[i]:
            tinysum += charpos(char.lower())

        bigsum += tinysum * (i + 1)

    print("Total of all name scores:", bigsum)
