#1. Write a program in Python to allow the error of syntax to be handled using exception handling.
try:
    def foo():
        return [1, 2, 3

    print(foo()
except SyntaxError:
    print("Hello")
#Not able to catch the syntax error

#2. Write a program in Python to allow the user to open a file by using the argv module. If the entered name is
# incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
import sys
try:
    f = open(sys.argv[1])
    print(f.read())
except IOError:
    print("Provided filename is incorrect")
except IndexError:
    print("Supply a filename as argument")

#3. Write a program to handle an error if the user entered a number more than four digits it should return
#  “The length is too short/long !!! Please provide only four digits”
a = input("enter 4 digit number: ")
if len(a) != 4:
    print("The length is too short/long !!! Please provide only four digits")

#4. Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password
# and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
username = "Manoramya"
password = "ramya1"
count = 0
while count < 3:
    username_input = input("enter a username")
    password_input = input("enter a password")
    if username_input == username and password_input == password:
        print("login success")
        count = 3
    else:
        print("Access denied, please reenter")
        count += 1

#6. Read doc.txt file using Python File handling concept and return only the even length string from
#the file. Consider the content of doc.txt as given below:
f = open('doc.txt', 'r')
for line in f:
    line = line.strip()
    if len(line) % 2 == 0:
        print(line)