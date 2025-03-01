import calculator
print("please select the operation you want to perform\n"\
      "1.add\n"\
        "2.subtract\n"\
            "3.multiply\n"\
                "4.divide\n"\
                    "5.power\n")
select= int (input("select operations from 1,2,3,4,5:"))
x=int(input("enter the first number"))
y=int(input("enter the second number"))
if select==1:
    ans=calculator.add(x,y)
elif select==2:
    ans=calculator.sub(x,y)
elif select==3:
    ans=calculator.mul(x,y)
elif select==4:
    ans=calculator.div(x,y)
elif select==5:
    ans=calculator.pow(x,y)
else :print("invalid input")

print(ans)