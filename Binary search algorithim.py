##Binary search algorithim (bisection method)
def bsearch(s, e, first, last):
    print (first, last)

    if (last - first) < 2:
        return s[first] == e or s[last] == e
    mid = first + (last - first) /2
    if s[mid] == e:
        return True
    if s[mid] > e:
        return bsearch(s, e, first, mid -1)
    return bsearch (s, e, mid +1, last)
