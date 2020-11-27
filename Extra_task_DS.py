# Extra task
import math

"""
1. Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list: [1, 2, 3, 4]
Access list: [600, 700]
Access list: [100, 300, 500, 600, 800]
Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list: [10]
Access list: [ ]
"""

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print(x[5][0:4])

print(x[6:8])

print(x[::2])

print([x[::-1]])

print([x[5][5][0]])

print([])

"""
2. Create a list of thousand numbers using range and xrange and see the difference between each
other.
(For reference:https://www.techbeamers.com/python-xrange-range/)
"""
## There is no xrange in python3

print(list(range(1,1001)))


"""
3. How Tuple is beneficial as compared to the list?
Ans: Tuple is immutable hence if wanted to enforce strict unchangebality to a list, tuple is the way to go.
    For example: list of allowed genders need to be stored, since that doesn't require to be changed tuple is good.
    Iteration over tuple is faster than list.
"""

"""
4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
the number which is divisible by 3 and is a multiple of 2.
"""

for i in range(1,101):
    if i % 3 == 0 and i % 2 == 0:
        print(i)

"""
5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
string with their index.
"""
str = "innovation"

reverse = str[::-1]

for i in range(len(str)):
    if reverse[i] in ["a", "e", "i", "o", "u"]:
        print("index", i, "string", reverse[i])

"""
6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
string which is having an even length.
"""

str2 = "hello my name is abcde"
for i in str2.split(" "):
    if len(i) % 2 == 0:
        print(i)


"""
7. Write a program in python to print the pair of numbers whose sum is equal to the result
number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
"""
x=[1,2,3,4,5,6,7,8,9,-1]

for i in x:
    for j in x:
        if not i >= j:
            if i + j == 8:
                print(i,j)

"""
8. Write a program in Python to complete the following task:
    - Create two lists such as even_list and odd_list.
    - Ask user to enter a number in the range of 1,50 and make sure if the entered number is
      even, append it to the even_list and if the entered number is odd append it to the odd_list.
    - Keep that in mind you can only add 5 items in each list.
    - Make sure once you enter all the 5 elements, calculate the sum of the list and return the
    maximum of the list.
"""

even_list = []
odd_list  = []
i = 0
while i < 10:
    a = int(input("enter a number between 1 and 50"))
    if a % 2 == 0 and len(even_list) <= 5:
        even_list.append(a)
    if a % 2 != 0 and not len(odd_list) >= 5:
        odd_list.append(a)
    print(even_list,odd_list)
    i += 1
print("even_sum", sum(even_list), "even_max", max(even_list))
print("odd_sum", sum(odd_list), "odd_max", max(odd_list))

"""
9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
Sample input: 12abcbacbaba344ab
Expected output: a=5 b=5 c=2
NOTE: Make sure to avoid counting the occurrence of numeric values in the string.
"""
d = {}
x = "12abcbacbaba344ab"
for i in x:
    if not i.isdigit() and not i in d:
        d[i] = x.count(i)
print(d)

"""
10. Generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10).
"""
lst = []
tpl = (1,2,3,4,5,6,7,8,9,10)
for i in tpl:
    if i % 2 == 0:
        lst.append(i)
print(tuple(lst))















