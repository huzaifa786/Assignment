inp=int(input("enter your range :"))
sum=0
s=0
for i in range(1,inp):

    sum+=1
    s+=i



for l in range(2,i):
    if(s % l == 0 and sum % l ==0 ):
        s=s//l
        sum=sum//l


print(sum,"/",s)