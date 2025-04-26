#randit()

# import random
# rand_numbers = []
# for i in range(10):
#     number = random.randint(1, 100)
#     rand_numbers.append(number)  
# print("List of random numbers:", rand_numbers)

# def calculate_average(numbers): 
#     total = sum(numbers)          
#     count = len(numbers)      
#     return total / count  

# average = calculate_average(rand_numbers)
# print("Average (calculation):", average)

# import statistics
# average_inbuilt_statistics = statistics.mean(rand_numbers)
# print("Average (inbuilt statistics.mean):", average_inbuilt_statistics)
# print("Are both averages the same?", average == average_inbuilt_statistics)

# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# def multiply(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     if num2 == 0:
#         return "Error! Cannot divide by zero."
#     return num1 / num2
 
# def calculator():
#     print("My Calculator!")
#     print("Available operations:")
#     print("1. Addition (+)")
#     print("2. Subtraction (-)")
#     print("3. Multiplication (*)")
#     print("4. Division (/)")

# while True:
#         choice = input("Enter operation number (1-4) or 'x' to quit: ")
#         if choice.lower() == 'x':
#             print("Ciao!")
#             break
        
#         if choice not in ['1', '2', '3', '4']:
#             print("Invalid choice. Please enter 1, 2, 3, or 4.")
#             continue
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except:
#             print("Invalid input. Please enter numbers only.")
#             continue
#         if choice == '1':
#             result = add(num1, num2)
#             print(f"Result: {num1} + {num2} = {result}")
#         elif choice == '2':
#             result = subtract(num1, num2)
#             print(f"Result: {num1} - {num2} = {result}")
#         elif choice == '3':
#             result = multiply(num1, num2)
#             print(f"Result: {num1} * {num2} = {result}")
#         elif choice == '4':
#             result = divide(num1, num2)
#             print(f"Result: {num1} / {num2} = {result}")

# import random

# print("Let's Play Guess!")
# print(" Guess the number I am currently thinking of between 1 and 100.")
# print("You've got 3 tries to guess it!")

# my_number = random.randint(1, 100)

# for attempt in range(1, 4):
#     print(f"\nAttempt {attempt} of 3")
#     while True:
#         try:
#             guess = int(input("Your guess: "))
#             if 1 <= guess <= 100:
#                 break
#             else:
#                 print("Please enter a number between 1-100.")
#         except:
#             print("That's not a number! Try again.")
    
#     # Check the guess
#     if guess == my_number:
#         print(f"Correct! You got it in {attempt} tries!")
#         break
#     elif guess < my_number:
#         print("Too low!")
#     else:
#         print("Too high!")
    
#     if attempt == 3:
#         print(f"\nGame over! The number was {my_number}.")

