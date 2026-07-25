name = "cindrella"
age = 67
place = "amsterdam"
integer = 13.33
print ("I live in", place)
place2 = place 
print (place2)
print (type(name))
print (type(age))
print (type(place))
print(type(integer))
old = True 
t = None
print (type(old))
print (type(t))
a = 75 
b = 29 
sum = a + b 
difference = a - b 
print ("the sum of a and b is ", sum)
print ("the difference of a and b is", difference)
#this is a comment.
#this too is comment.

 
#Arithmetic operators 
a = 8
b = 7
print ("a + b =", a+b) #addition
print ("a-b =", a-b) #subtraction
print ("a x b =", a*b) #multiplication
print ("a/b =", a/b) #division 
print ("a^b =" , a**b) #exponent 
print ("remainder of a/b =", a%b) #modulus

#relational operators
print ("a > b is", a>b) #greater than 
print ("a < b is" , a<b) #less than 
print ("a != b is" , a != b) #not equal to
print ("a == b is" , a == b) #equal to 
print ("a >= b is" , a >= b) #greater than or equal to 
print ("a <= b is" , a <= b) #less than or equal to 

#assignment operators
num = 9 
num += 7 #num = num + 7
print ("num is", num)
num1 = 15 
num1 -= 8 #num1 = num1 - 8 
print ("num1 is", num1)
num2 = 17 
num2 *= 8 #num2 = num2 * 8 
print ("num2 is" , num2)
num3 = 95 
num3 %= 6 #remainder of 'num3' divided by 6 
print ("num3 is", num3)
num4 = 68 
num4 **= 10 #68 raised to the power of 10 
print ("num4 is", num4)

#logical operators 
a = 50
b = 25
print (not (a>b)) #NOT operator 

print (not False) #NOT operator 
print (not True) #NOT operator 

val1 = True
val2 = False 
print ("ans operator is" , val1 and val2) #AND operator (true = only if both operands are true , if not false)
print ("ans operator is" , val1 or val2) #OR operator (true = if at least one operand is true , if not false) 

print ("ans operator is" , (a==b) or (a>b)) #example of OR operator 
print ("ans operator is" , (a==b) and (a>b)) #example of AND operator 

#type conversion 
a = 5
b = 6.5 
print ("a is of type" , type(a)) #type of 'a' is integer 
print ("b is of type" , type(b)) #type of 'b' is float
print ("a + b is " , a+b) #result is of type float because of type conversion 
 #example of type conversion
c = int("28") #string to integer(basically we jst converted the string "28" to the integer 28 by using the function 'int()')
d = 9.8 
print ("c is of type" , type(c)) #type of 'c' is integer 
print ("d is of type" , type(d)) #type of 'd' is float
print ("c + d is" , c+d) #result is of type float because of type conversion 
e = float(90) #integer to float (we converted the integer 90 to the float 90.0000 by using the function 'float()')
f = 47.3763 
print ("e is of type" , type(e))
print ("f is of type" , type(f))
print ("e + f is" , e+f) #result is of type float because of type conversion 
j = str(56) #integer to string (we coverted the integer 56 to the string "56" by using the function 'str()')
k = "33"
print ("j is of type" , type(j)) #type of 'j' is string
print ("k is of type" , type(k)) #type of 'k' is string
print ("j + k is" , j+k) #result is of type string because of type coversion (we concatenated the two strings "56" and "33" to get "5633")

#inputs in python 
#examples
name = input("enter your name: ") #input function basically takes input from user 
print("welcome" , name) #we can also concatenate the string "welcome" with the variable 'name' to get a personalised welcome msg for the user 
age = int(input("enter your age: ")) #we can also convert the input to integer by using the function 'int()'
print ("your age is" , age) #we can also concatenate the string "your age is" with the variable 'age' to get a personalised display of the user's age
val = (input("enter a value: ")) #to know the type of the input value we can use the function 'type()' 
print(type(val),val) #and by using the function 'print()' we can display the type of the input value along with the value itself
#from the above code we can see that the input value is of type string because by default the input function takes the input as a string unless we specify otherwise by using type conversion functions like 'int()' or 'float()' etc.
price = float(input("enter the price of the item: ")) #we can also convert the input to float by using the function 'float()'
print("the price of the item is" , price) #we can also concanate the string "the price of the item is" with the variable 'price' that we go from the user to get a personalised display of the price of the item
#here doesn't matter if the user enters the price as an integer or a float because we have concated the input with the function 'float()' so even if the user enters an integer value for the price it will be converted to float and we will get the price in float format in the output.
#exampleee (like if we wanna put a student name,class,marks in %)
Name = input("Name:" ) #user can put his/her name here and it will be stored in the variable 'Name' and we can use that variable to display the name of the user in the output
Class = int(input("Class:")) #user can put his/her class here and it will be stored in the variable 'Class' and we can use that variable to display the class of the user in the output
Marks = float(input("Marks(in %):"))#user can put his/her marks in percentage here and it will be stored in the variable 'Marks' and we can use that variable to display the marks of the user in the output 
print("Welcome", Name) #we can also concatenate the stering "Welcome" with the variable 'Name' to get a personalised welcome message for the user
print("from Std.", Class) #we can also concatenate the string "from Std." with the variable 'Class' to get a personalised display of the user's class
print("congrats you got" , Marks) #we can also concatenate the string "congrats you got" with the variable 'Marks' to get a personalised display of the user's marks in percentage 

#let's practice(from lec-1);
 #1.Write a program to input two numbers & print their sum.
num5 = float(input("enter the first number: ")) 
num6 = float(input("enter the second number: "))
sum1 = num5 + num6
print("the sum of the given two numbers is" , sum1)
 #2.Write a program to input the side of a square & print its area.
side = float(input("enter the side of the square: "))
Ar = side*side 
print("the area of the square is" , Ar)
 #3.Write a program to input two floats & print their average.
num7 = float(input("enter the first number: "))
num8 = float(input("enter the second number: "))
avg = (num7 + num8)/2
print("the average of the above two numbers is" , avg)
 #4.Write a program to input 2 integer numbers,a and b , print true if a is >= b ,else print false.
a = int(input("enter the firsst number: ")) 
b = int(input("enter the second number: "))
print(a>=b)









