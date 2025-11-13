# print("output:" ,not False)
# print ("output:" ,not True)
# a= 12
# b=15
# print ("Ans is :",a==b)
# print ("Ans is :",not a>b)
# print ("Ans is :",not a<b)

# # AND operator
# val1 = False 
# val2 = False
# print ("Ans is :",val1 and val2)

#OR operator

# Initialize an empty dictionary
# squares_dict = {}

# # Iterate through numbers from 1 to 15
# for number in range(1, 16):
#     # Calculate the square of the number
#     square = number ** 2
#     # Add the number and its square to the dictionary
#     squares_dict[number] = square

# # Print the resulting dictionary
# print(squares_dict)


# dict ={}
# for i in range(1, 16):
#     squre = i**2
#     dict[i]= squre
# print(dict)


# a,b =4,5
# txt = "=+"
# c=(a*txt*b)
# print(c)
# print(f"It's used : {c.count(txt)} times")



# def intro(name, age, city):
#     print(f"My name is {name}, I'm {age} years old and I live in {city}.")

# p = {
#     "name": "Prajjwa'",
#     "age": 23,
#     "city": "Prayagraj"
# }

# intro(**p)












# calculator.py

# Functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Main program loop
while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    # Take user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice! Please select from 1 to 5.")
