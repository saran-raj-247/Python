s=input()
n=int(input())
a=s.split()
l=len(a)
count=0
for i in a:
    p=len(i)
    if(p>=n):
        count=count+1
print(count)        
