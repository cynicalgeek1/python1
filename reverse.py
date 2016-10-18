m=[]
w=input("enter word:")
m.append(w)
l=len(w)
c=1
while c<=l:
    print(w[l-c],end='')
    c+=1
print()
m.reverse()
