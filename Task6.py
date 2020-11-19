#1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
sample_str = "PythonTraining"
print("Original string is: ", sample_str)

res = [char for char in sample_str if char.isupper()]
print("Upper case characters in string: ", res)

#2. Write a program to construct a dictionary from the two lists containing the names of students and
#their corresponding subjects. The dictionary should map the students with their respective subjects.
#Let’s see how to do this using for loops and dictionary comprehension.
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
print("students list is : ", students)
print("Subjects list is : ", subjects)
res = {}
for i in students:
    for j in subjects:
        res = dict(zip(students,subjects))
print("Resultant dictionary is : ", res)

#3. Learn More about Yield, next and Generators

#4. Write a program in Python using generators to reverse the string.
#Input String = “Consultadd Training”
def reverse_string(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]
for char in reverse_string("Consultadd Training"):
    print(char)

#5. Write an example on decorators.
def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    return inner1


@hello_decorator
def myfunc():
    print("Hi this is function")
