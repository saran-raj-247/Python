x=int(input())
y=int(input())
z=int(input())
if(((x**2)+(y**2))==(z**2)):
    print("yes")
elif(((y**2)+(z**2))==(x**2)):
    print("yes")
elif(((x**2)+(z**2))==(y**2)):
    print("yes")
else:
    print("no")