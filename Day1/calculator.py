#import arithmetic
#import arithmetic as arith
#from arithmetic import add_numbers, subtract_numbers
#from arithmetic import *
from Day1.arithmetic import add_numbers as add,multiply_numbers as multiply, subtract_numbers as subtract, divide_numbers as divide


num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))
sum: int = add(num1, num2)
product: int = multiply(num1, num2)
difference: int = subtract(num1, num2)
quotient: float = divide(num1, num2)

print(f"The sum of {num1} and {num2} is: {sum}")
print(f"The product of {num1} and {num2} is: {product}")
print(f"The difference of {num1} and {num2} is: {difference}")
print(f"The quotient of {num1} and {num2} is: {quotient}")