a=input()
b=input()
print(list(int(a)))
print(list(int(b)))


L1=[]
L2=[]
L1.append(a)
L2.append(b)
if L1 in L2 or L2 in L1:
    print("True")
else:
    print("False")