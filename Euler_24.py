

def permutation(s):

    # If s is empty then there are no permutations
    if len(s) == 0:
        return []

    # If there is only one element in s then, only
    # one permuatation is possible
    if len(s) == 1:
        return [s]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(s) and calculate the permutation
    for i in range(len(s)):
       m = s[i]

       # Extract s[i] or m from the list.  remLst is
       # remaining list
       remLst = s[:i] + s[i+1:]

       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l

if __name__ == "__main__":

    base = list("1234567890")
    strperm = []

    for p in permutation(base):
        strperm.append("".join(p))

    strperm = sorted(strperm)

    print("{} is the one millionth lexicographic permutation of the digits 0-9".format(strperm[999999]))
