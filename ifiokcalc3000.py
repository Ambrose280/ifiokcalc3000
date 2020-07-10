def add(x, y):
   return(x + y)

def subtract(x, y):
   return(x - y)

def mult(x, y):
   return(x * y)

def div(x, y):
   return(x / y)
import math
import cmath

myname = input("Hi there! What's your name?:")
print("It's nice to meet you, " + myname)
print("Your name is " + str(len(myname)) +  str(" letters") + str(" long"))
print("Anyway that's not what you're here for, Welcome to IfiokCalc3000")
print("Enter 1 to perform addition")
print("Enter 2 to perform a subtrction between two numbers")
print("Enter 3 to perform multiplication between two numbers")
print("Enter 4 to perform division between  two numbers")
print("Enter 5 to Calculate Square root of any number")
print("More functions will be added later")
choice = input("Choose a function 1/2/3/4:")
while True:
   if choice in('1', '2', '3', '4',):
      num1 = int(input("Enter first number:"))
      num2 = int(input("Enter second number:"))
   if choice == "1":
         print(num1, "+", num2, "=", add(num1, num2))
         break
   elif choice == "2":
         print(num1, "-", num2, "=", subtract(num1, num2))
         break
   elif choice == "3":
         print(num1, "*", num2, "=", mult(num1, num2))
         break
   elif choice == "4":
         print(num1, "/", num2, "=", div(num1, num2))
         break
   
