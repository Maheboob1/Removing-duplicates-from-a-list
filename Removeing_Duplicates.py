duplicates=[1,2,3,3,3,3,4,5]
def Remove(duplicates):
    L1=[]
    for num in duplicates:
        if num not in L1:
            L1.append(num)
    print(L1)

Remove(duplicates)