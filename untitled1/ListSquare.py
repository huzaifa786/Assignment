list=[]
List2=[]
counter=0

while 1:
    inp=input("Enter your number :")
    if(inp=="done"):
        break
    inp=int(inp)
    list.append(inp)
    sq=inp*inp
    List2.append((list[counter],sq))
    counter+=1
print(list)
print(List2)