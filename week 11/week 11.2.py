try:    
    a=int(input())
    b=int(input())
    if(a>0 and b>0):
        c=a/b
        d=a%b
        print('Division result:',c)
        print('Modulo result:',d)
    else:
        print('Error: Cannot divide or modulo by zero.')
except ValueError:
    print('Error: Non-numeric input provided.')
