def add (number1 , number2):
    sum = number1+number2
    return sum

def sub (number1 , number2):
    sum = number1-number2
    return sum

num1 = int(input("Enter your first num: "))
num2 = int(input("Enter your second num: "))
sum_add = add(num1 , num2)  
print("additional result is:" , sum_add)

sum_sub= sub(num1 , num2)  
print("subtraction result is:" , sum_sub)