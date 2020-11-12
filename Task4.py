#1. Write a program to reverse a string.
s = 'consultadd'
print(s[::-1])

#2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
def get_upp_low(s):
    u = 0
    l = 0
    for i in s:
        if i.isupper():
            u+=1
        if i.islower():
            l+=1
        else:
            pass
    print("upper case letters: ", u)
    print("lower case letters: ", l)

a = input("enter a string")
get_upp_low(a)

#3. Create a function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    a = []
    for i in l:
        if i not in a:
            a.append(i)
    return a
print(unique_list([1,2,3,2,4,5,6,4]))

#4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated
# sequence after sorting them alphabetically.
def sequence_words(s):
    lst=s.split("-")
    lst.sort()
    return "-".join(lst)
a=input("enter a hyphen-seperated string")
print(sequence_words(a))

#5. Write a program that accepts a sequence of lines as input and prints the lines after making all
#characters in the sentence capitalized.
a = input("enter string: ")
print(a.upper())

#6. Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.
def calculatesum(a,b):
    s = int(a) + int(b)
    return s
n1 ="10"
n2 = "20"
print(calculatesum(n1,n2))

#7. Define a function that can accept two strings as input and print the string with the maximum length in the console.
# If two strings have the same length, then the function should print both the strings line by line.
def compare_strings(s1,s2):
    if len(s1) == len(s2):
        print(s1)
        print(s2)
    elif len(s1) > len(s2):
        print(s1)
    else:
        print(s2)
a= input("enter string1")
b= input("enter string2")
compare_strings(a,b)

#8. Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).
def printsquares():
    l = []
    for i in range(1,21):
        l.append(i*i)
    print(tuple(l))
printsquares()

#9. Write a function called showNumbers that takes a parameter called limit. It should print all the
#numbers between 0 and limit with a label to identify the even and odd numbers.
def shownumber(limit):
    i = 0
    while i <= limit:
        if i%2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

        i+=1
shownumber(5)

#10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
def filtereven(number):
    if number % 2 == 0:
        return True
    return False

lst = list(range(1, 21))
resultant_even = filter(filtereven, lst)

print(list(resultant_even))

#11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
lst = [1,2,3,4,5,6,7,8,9,10]
a= list(map(lambda i: i**2, (list(filter(lambda n: n%2==0, lst)))))
print(a)

#12. Write a function to compute 5/0 and use try/except to catch the exceptions
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why you are dividing a number by ZERO!!")
except:
    print("Any other exception")

#13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
L= [1,2,3,4,5,6,7]
a=reduce(lambda a,b:10*a+b, L, 0)

#14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
#Make sure to use only higher order functions.
lst= list(range(1,100))
a=list(filter(lambda n: n%7==0 and not n%3==0, lst))
print(a)

#15. Write a program in Python to multiply the elements of a list by itself using a traditional function
#and pass the function to map() to complete the operation.

#16. What is the output of the following codes:
#(!) 2
#(!!)NameError







