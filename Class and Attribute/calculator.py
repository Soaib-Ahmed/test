class Calculator:
    def add(self,x,y):
        return x+y

    def substract(self,x,y):  
        return x-y  

    def mult(self,x,y):  
        return x*y

    def divides(self,x,y):
        return x/y

calc=Calculator()

result_add = calc.add(5, 3)
print("Addition:", result_add)

result_subtract = calc.substract(8, 2)
print("Subtraction:", result_subtract)

result_multiply = calc.mult(4, 7)
print("Multiplication:", result_multiply)

result_divide = calc.divides(10, 2)
print("Division:", result_divide) 