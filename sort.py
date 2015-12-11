'''Program to solve to sort a list'''
def sorter(lst):
    j=1
    count=0
    for x in range(0,len(lst)):
        for y in range(j,len(lst)):
            if lst[x]>lst[y]:
                temp=lst[x]
                lst[x]=lst[y]
                lst[y]=temp

        count+=1
        j=count+1

    return lst
                
