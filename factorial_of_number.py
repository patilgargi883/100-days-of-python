#factorial of number
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
num=int(input("enter the number"))
print("The factorial of the",num,"is",fact(num))