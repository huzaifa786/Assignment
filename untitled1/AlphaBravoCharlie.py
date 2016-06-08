

for i in range(1,110):
    if (i%11==0):
        print('\n')
    elif(i%3==0):
        print(" alpha ",end='')
    elif(i%5==0):
        print(" bravo ",end='')
    elif(i%7==0):
        print(" charlie ",end='')
    elif(i%3 ==0 and i%5== 0):
        print(" alpha bravo",end='')
    else:
        print(i," ",end='')