a=input()
a=a.split()
if a=="Hello World":
    print("WORLD")
elif len(a)==1:
    print("LESS")
else:
    print(a[1].upper())
