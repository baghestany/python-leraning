


def  Fac(x):
     f=1
     for i in range(1,x+1):
         f=i*f
     return f




x = int(input("Please enter a number:"))
print(f"Factorial of {x}: " , Fac(x))

