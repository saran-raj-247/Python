t=int(input())
for i in range(t):
    str1=input().lower()
    str2=input().lower()
    if str1 < str2:
        print("-1")
    elif str1 > str2:
        print("1")
    else:
        print("0")
