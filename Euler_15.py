from math import factorial

def choose(n,k):
    return factorial(n) // factorial(k) // factorial(n-k)

if __name__ == "__main__":
    #this is a combinatorics problem
    #n choose k
    print("There are {} paths in a 20x20 grid".format(choose(400,20)))
