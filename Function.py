def op_marker():
    n=int(input("Enter an Option: "))
    if n>0 and n<6:
       a=int(input())
       b=int(input())
       if n==1:
        k=a+b
       elif n==2:
         k=a-b
       elif n==3:
         k=a*b
       elif n==4:
         k=a/b
       elif n==5:
         k=a%b
    else:
      k="Invalid Input"
    print(k)
op_marker()