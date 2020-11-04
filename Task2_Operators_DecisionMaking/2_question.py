#Second Problem
print("""Enter 1 for Addition
Enter 2 for Subtraction
Enter 3 for Multiplication
Enter 4 for Division
Enter 5 for Average""")

choice = int(input("Enter a choice: "))
num1 = int(input("Enter first  number: "))
num2 = int(input("Enter second number: "))

result = None
if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    result = num1 / num2
elif choice == 5:
    result = (num1 + num2) / 2
else:
    print("Invalid choice")

if result is not None:
    print(f"Result is : {result}")
    if result < 1:
        print("NEGATIVE")

