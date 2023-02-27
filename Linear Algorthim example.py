##Linear search on this one is slow

def search(s, e):
    answer == None
    i = 0
    numCompares = 0
    while i < len(s) and answer == None:
        numCompares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i += 1
    print ('Answer: ', answer, 'Number of compares: ', numcompares)

