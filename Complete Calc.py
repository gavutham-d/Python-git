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
    elif n=='^':
        k=a
        while b>1:
            k=k*a
            b=b-1
        s=k
    else:
        s='Invalid Operator'
    print(s)
option()