a=int(input('enter your number :'))
p=str(a)
list=[]
for i in p:
    k=a%10

    list.append(k)
    a=int(a/10)

print(list)