#Calculator
class Calculator:
    def __init__(self):
        pass
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        return round(a/b,2)
if __name__=="__main__":
    c=Calculator()
    while(True):
        print("----Simple Calculator----")
        print("1.Additon \n2.Subtraction \n3.Multiplication \n4.Division")
        op=int(input("Enter your option :"))
        a=int(input("Enter first number :"))
        b=int(input("Enter second number :"))
        if op==1:
            r=c.addition(a,b)
        elif op==2:
            r=c.subtraction(a,b)
        elif op==3:
            r=c.multiplication(a,b)
        elif op==4:
            r=c.division(a,b)
        print("Result =",r)
        choice=input("Do you want to Continue(Y/N):")
        if choice.lower()=="y":
            continue
        else:
            break
