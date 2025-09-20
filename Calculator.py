def option():
    a=int(input())
    b=int(input())
    n=input("Enter the Operator: ")
    if n=='+':
        s=a+b
    elif n=='-':
        s=a-b
    elif n=='*':
        s=a*b
    elif n=='/':
        s=a/b
    elif n=='%':
        s=a%b
    else:
        s='Invalid Operator'
    print(s)
option()