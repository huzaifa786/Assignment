import itertools
counter=0
sum=0
opt=int(input('Press 1 for while loop else 2 for for loop',))

if(opt==1):
    print("For loop running : ")
    for i in itertools.count():
        inp=input('enter :')
        if (inp=="done"):
            break
        inp=int(inp)

        sum+=inp
        counter+=1

elif(opt==2):
    print("while loop running :")
    while 1:
        inp=input('enter :')
        if (inp=="done"):
            break
        inp=int(inp)

        sum+=inp
        counter+=1



    avg=sum/counter
    print('sum =',sum)
    print('avg = ',avg)