a=input("Enter first number:")
operator=input("Enter operator(+,-,/,*,%):" )
b=input("Enter second number:")

if operator=='+':
    print(int(a)+int(b))
elif operator=='-':
    print(int(a)-int(b))
elif operator=='/':
    print(int(a)/int(b))
elif operator=='%':
    print(int(a)%int(b))
elif operator=='*':
    print(int(a)*int(b))

else:
    print("Inalid input")  
