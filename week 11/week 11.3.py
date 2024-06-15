try:    
    a=float(input())
    b=float(input())
    c=a/b
    print(c)
except ZeroDivisionError:
    print('Error: Cannot divide or modulo by zero.')
except ValueError:
    print('Error: Non-numeric input provided.')
