#1. Python Basics
name = "Ali"
age = 21
cgpa = 3.5
is_student = True
print(name)
print(age)
print(cgpa)
print(is_student)

#operators
a = 10
b = 5
print(a + b)
print(a > b)
print(a > b and b > 0)

#2. Conditional Statements
age = 18
if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible")

 #3.For Loop
    for i in range(1, 6):
    print(i)

# while loop
count = 1

while count <= 5:
    print(count)
    count += 1

#4.Function
def greet(name):
    print("Hello", name)

greet("Ali")

# Function with retun value
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

#5. Lists and Dictionaries

#List Example
fruits = ["Apple", "Mango", "Banana"]
print(fruits[0])

#Dictionary Example
student = {
    "name": "Ali",
    "age": 21
}
print(student["name"])

#6. Problem Solving Practice
 #Problem 1: Even or Odd
 num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

 #Problem 2: Find Largest Number
 a = 10
b = 25
if a > b:
    print(a)
else:
    print(b)

 #Problem 3: Sum of First N Numbers
 n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)
