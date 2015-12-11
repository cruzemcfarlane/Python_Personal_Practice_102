def sumlist(n):
    y=0
    for x in n:
        y=y+x
    return y

def sumlist2(n):
    y=0
    for x in range(len(n)):
        y=y+n[x]
    return y

def sumlist3(n):
    if n==[]:
        return 0
    else:
        return 1+sumlist3(n[1:])

def maxlist(n):
    if n==[]:
        return 0
    else:
        return max(n[0],maxlist(n[1:]))
