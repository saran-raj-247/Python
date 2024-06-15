try:
    a=int(input())
    if(a>0 and a<=100):
        print("Valid input.")
    else:
        print("Error: Number out of allowed range")
except ValueError:
    
       print("Error: invalid literal for int()") 
