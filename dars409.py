# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             raise ValueError("Age must be a non-negative integer")
#
# person = Person("Ali", 30)
# print(person.get_name())
# print(person.get_age())
#
# person.set_name("Vali")
# person.set_age(25)
# print(person.get_name())
# print(person.get_age())
# class Temperature:
#     def __init__(self, celcius):
#         self.__celcius = celcius
#
#     def get_celcius(self):
#         return self.__celcius
#
#     def set_celcius(self, celcius):
#         self.__celcius = celcius
#
#     def to_fahrenheit(self):
#         return (self.__celcius * 9/5) + 32
#
# temp = Temperature(-25)
# print(temp.get_celcius())
# print(temp.to_fahrenheit())
#
# temp.set_celcius(0)
# print(temp.to_fahrenheit())
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.__balance = initial_balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: ${amount:.2f}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew: ${amount:.2f}")
#         else:
#             print("Invalid withdrawal amount.")
#
#     def get_balance(self):
#         return self.__balance
#
# account = BankAccount(100)
# print(f"Current Balance: ${account.get_balance():.2f}")
#
# account.deposit(50)
# print(f"Current Balance: ${account.get_balance():.2f}")
#
# account.withdraw(30)
# print(f"Current Balance: ${account.get_balance():.2f}")
# account.withdraw(200)
# class StudentGrades:
#     def __init__(self, name):
#         self.__name = name
#         self.__grades = []
#
#     def add_grade(self, grade):
#         if isinstance(grade, (int, float)) and 0 <= grade <= 100:
#             self.__grades.append(grade)
#             print(f"Added grade: {grade}")
#         else:
#             print("Grade must be a number between 0 and 100.")
#
#     def get_average(self):
#         if not self.__grades:
#             return 0
#         return sum(self.__grades) / len(self.__grades)
#
#     def get_name(self):
#         return self.__name
#
# student = StudentGrades("VASTELORD")
# student.add_grade(85)
# student.add_grade(90)
# student.add_grade(75)
#
# print(f"{student.get_name()}'s average grade: {student.get_average():.2f}")
# class Car:
#     def __init__(self, make):
#         self.__make = make
#         self.__fuel_level = 0
#
#     def add_fuel(self, amount):
#         if amount > 0:
#             self.__fuel_level += amount
#             print(f"Added fuel: {amount} liters. Current fuel level: {self.__fuel_level} liters.")
#         else:
#             print("Fuel amount must be greater than zero.")
#
#     def drive(self, distance):
#         fuel_needed = distance * 0.1
#         if fuel_needed <= self.__fuel_level:
#             self.__fuel_level -= fuel_needed
#             print(f"Driving {distance} kilometers. Fuel used: {fuel_needed} liters. Remaining fuel: {self.__fuel_level} liters.")
#         else:
#             print("Not enough fuel to drive the requested distance.")
#
#     def get_fuel_level(self):
#         return self.__fuel_level
#
#     def get_make(self):
#         return self.__make
#
# my_car = Car("Toyota")
# my_car.add_fuel(20)
# my_car.drive(150)
# my_car.drive(100)
# print(f"Current fuel level: {my_car.get_fuel_level()} liters.")