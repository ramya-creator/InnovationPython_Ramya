#1. Create a list of 10 elements of four different data types like int, string, complex and float.
elements= [1,3,5,'ramya','consultadd','python',1+3j,2+6j,3.5,2.7]

#2. Create a list of size 5 and execute the slicing structure
a=[1,2,3,4,5]
print(a[1:4])

#3. Write a program to get the sum and multiply of all the items in a given list.
a=[1,2,3,4,5]
total_sum=0
total_product=1
for i in a:
    total_sum+=i
    total_product*=i
print(total_sum,total_product)

#OR using reduce
from functools import reduce
tot_sum = reduce(lambda x,y:x+y, a)
tot_mul = reduce(lambda x,y:x*y, a)
print(tot_sum,tot_mul)

#4. Find the largest and smallest number from a given list.
a=[1,2,3,4,5]
largest = max(a)
smallest = min(a)
print(largest,smallest)

#5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
a=[1,2,3,4,5]
a_even=[]
for i in a:
    if i%2 == 0:
        a_even.append(i)
print(a_even)

#6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and 30 (both included).
x=[]
for i in range(1,31):
    x.append(i*i)
print(x[:5]+x[-5:])

#7. Write a program to replace the last element in a list with another list.
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l1[-1:] = l2
print(l1)

#8. Create a new dictionary by concatenating the following two dictionaries:
d1 = {1:10,2:20}
d2 = {3:30,4:40}
d3 = {}
for d in (d1,d2):
    d3.update(d)
print(d3)

#9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
n = int(input("enter a number"))
d = {}
for x in range(1,n+1):
    d[x]=x*x
print(d)

#10. Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.
n = input('enter comma-seperated numbers')
l = n.split(",")
t = tuple(l)
print('list: ',l)
print('tuple:',t)







