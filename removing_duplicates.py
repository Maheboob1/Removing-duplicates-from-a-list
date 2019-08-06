duplicates=[5,6,5,6,4,2,8,4,8,1,7,9,9]
def remove(duplicates):
    L1=[]
    L2=[]

    for num in duplicates:
        if num not in L1:
            L1.append(num)
        else:
            L2.append(num)

    print(L1)
    print(L2)

remove(duplicates)