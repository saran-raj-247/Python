a=int(input())
sum=a+1
k=-1
for i in range(0,a):
    if(k==1):
         break
    d=i*i
    if(d==sum):
        k=1
    else:
        k=0
if(k==1):
    print("Yes")
else:
    print("No")
