a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(a):
    L1=[]
    L2=[]
    for i in a:
        if i%2==0:
            L1.append(i)
        else:
            L2.append(i)
    print(L1)
    print(L2)

even(a)