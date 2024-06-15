try:
    a=int(input())
    if(a<0):
        print("Error: Please enter a valid age.")
    else:
        print("You are",a,"years old.")
except EOFError:
    print("Error: Please enter a valid age.")
except ValueError:
    print("Error: Please enter a valid age.")
