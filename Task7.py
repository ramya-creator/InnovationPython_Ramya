"""1. Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D is a variable whose values should be input to your program in a comma-separated sequence.
"""
import math
C = 50
H = 30
result = []
D = input("enter numbers seperated by ',': ")
Ds = D.split(',')
Ds = [int(a) for a in Ds]
for i in Ds:
    Q=math.sqrt((2*C*i)/H)
    result.append(Q)
print(result)

"""2. Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default."""
class shape():
    def __init__(self):
        pass
    def area(self):
        print(0)

class square():
        def __init__(self, length):
            self.length = length
        def area(self):
            a = (self.length * self.length)
            print("Area of square:", a)

s = square(2)
print(s.area())
print(shape().area())

#3. Create a class to find three elements that sum to zero from a set of n real numbers
arr = [-25,-10,-7,-3,2,4,8,10]
n = len(arr)
def findTriplets(arr, n):
    f = True
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    f = True

    if (f == False):
        print(" not exist ")

findTriplets(arr, n)

"""4. Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
Create another method displayTime which should print the time.
Also create a method displayMinute which should display the total minutes in the Time.
"""
class Time:
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
    def addTime(t1,t2):
        t3 = Time(0,0)
        t3.hours = t1.hours + t2.hours
        t3.minutes = t1.minutes + t2.minutes
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3
    def displayTime(self):
        print("Time is %d hours and %d minutes" %(self.hours, self.minutes))
    def displayMinute(self):
        print((self.hours*60) + self.minutes, "minutes")

a = Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()

"""#5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
methods:
yearPasses() should increase age by the integer value that you are passing inside the function.
amIOld() should perform the following conditional actions:I
f age is between 0 and <13, print “You are young”.
If age is >=13 and <=19 , print “You are a teenager”.
Otherwise, print “You are old”."""
class Person:

    def __init__(self,age):
        if age<0:
            print("Age is not valid, setting age to 0")
            self.age=0
        else:
            self.age=age

    def yearPasses(self,increase):
        self.age += increase
        return self.age

    def amIOld(self):
        if self.age>=0 and self.age<13:
            print("You are young")

        elif self.age>=13 and self.age<=19:
            print("You are a teenager")

        else:
            print("You are old")

age=[-1,4,10,16,18,64,38]
for i in age:
    a=Person(i)
    a.amIOld()
a=Person(38)
print(a.yearPasses(4))

