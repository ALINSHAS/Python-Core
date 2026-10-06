#write a program to find BMI(Body Mass Index)
# Weight = float(input("Enter your weight in kg \n"))
# Height = float(input("Enter your height in m \n"))
# BMI = Weight / (Height**2)
# if(BMI<=18.4):
#     print("underweight")
# elif(18.5<=BMI<=24.9):
#     print("Normal")
# elif(25<=BMI<=39.9):
#     print("Overweight")
# elif(BMI>=40):
#     print("Obese")
# else:
#     print("Invalid")

#2.# A toy vendor supplies three types of toys:
# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,
# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.
# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
# item=input("enter the item \n 1 - Battery toy\n 2 - Key toy \n 3 - ELectrical Charged toy\n")
# amount=float(input("Enter the amount \n"))
# if(item == "1"):
#     if(amount>1000):
#         amount=amount-(amount*(10/100))
#         print(amount)
#     else:
#         print(amount)
#     if(amount > 100):
#         amount = amount -(amount*(5/100))
#         print(amount)
#     else:
#         print(amount)
# elif(item == "3"):
#     if(amount > 500):
#         amount = amount -(amount*(10/100))
#         print(amount)
#     else:
#         print(amount)
# else:
#     print("invalid")

#3 FIZZBUZZ Problem
# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

# FizzBuzz Program

# n=int(input("enter a number"))
# if(n%3==0):
#     if(n%5==0):
#         print("fizzbuzz")
#     else:
#         print("fizz")
# elif(n%5==0):
#     print("buzz")
# else:
#     print(n)    
       