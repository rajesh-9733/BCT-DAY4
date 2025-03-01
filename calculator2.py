import calculator
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
operation1=input("choose the operation 1.+ \n 2.- \n 3.* \n 4./ \n")
if operation1=='1':
    a=calculator.add(num1,num2)
    print(a)
elif operation1=='2':
    a=calculator.sub(num1,num2)
    print(a)
elif operation1=='3':
    a=calculator.mul(num1,num2)
    print(a)
elif operation1=='4':
    a=calculator.div(num1,num2)
    print(a)   