#strings in python
#string is a data type which stores a sequence of characters (letters , numbers , symbols)
str1 = "Hello World" #string can be defined using double , single or triple quotes depending upon the requirement
str2 = "Python's a great language" #we used double quotes to define the string because it contains a single quote (apostrophe) in it
str3 = 'She said "python is cool"' #we used single quotes to define the string because it contains double quotes in it 
str4 = """or she can say 'doubt is tool'""" #we used triple quotes to define the string because it contains both single and double quotes in it 
print (str1)
print (str2)
print (str3)
print (str4)

#use of \n in string 
str5 = "duck duck \ngoose" #\n is used to create a new line in the string 
print (str5)

#use of \t in string 
str6 = "name\tage\tcity" #\t is used to create a tab space in the string
print (str6)

#concatenation of strings (joining of strings)
str7 = "Madhu"
str8 = "sudan"
print (str7 + str8) #we can concatenate two strings using the '+' operator 
#another example 
str9 = "Dog"
str10 = "esh"
example1 = str9 + str10 #we can also concatenate two strings and store the result in a new variable 
print (example1)

#length of string 
print ("length of str1 is" , len(str1)) #we can find the length of a string using the function 'len()' 
#note: the length of a string is the number of characters in it including spaces and special characters
#example 
str11 = "python"
str12 = "programming"
str13 = str11 + str12 #we can also concatenate two strings & the find the length of the concatenated string 
print (str13)
print ("length of str11 is" , len(str11))
print ("length of str12 is" , len(str12))
print ("length of str13 is" , len(str13))
#use of " "(this is used to define space between words in output)
str14 = str11 + " " + str12
print(str14)

#index in python (index basically means the position in python)
#NOTE:While giving postion in python it always starts from 0 rather than 1,and any special chars or space also gonna take a position.
str15 = "go to college"
print(str15[2]) #here we can see that space does take a different postion
print(str15[0]) #here we can see that the first position is 0th rather than 1st
print(str15[9]) #and yeah its basically normal

#slicing (accessing parts of a string)
#str[starting_idx:ending_idx] #ending idx is not included 
str15 = "mechanicalthings"
print(str15[1:5]) #it will print 'echa' and 'n' won't be there cause end index isn't included
print(str15[0:10]) #it will print from the 0th position to 9th position
print(str15[0:]) #it's also another way to get output from the starting till the end position of the string  
#negative index (In python we can also count the position in backwards direction like the endmost alphabet will be considered/positioned as '-1' then '-2',... as well as the end index in sytax will not be included as it used to be..)
print(str15[-9:-1])
print(str15[-9:]) #it should print till the end as used to before..
 
#string functions
#example
str16 = "I'm a coder"
print(str16.endswith("er")) #prints true if the given string ends with given substring like for here it's "er" (substring is the chhota wala part of string you can consider)
print(str16.endswith("joker")) #as the string doesn't contain joker in the end it'll show false
str17 = "wutt you sayinn?"
print(str17.capitalize()) #it creates a new string in the output in which the starting of the alphabet or 1st alphabet of given string gets capitalized
print(str17) #if we print again the given string it'll still show up wid the small letter but if we want to make it permanent like we want that  whenever we print it should show up wid capitar alphabet first then we just have to assign a str which will be equal to the capitalize wala code as given below the example.
str17 = (str17.capitalize()) 
print(str17) #yeah like here it just capitalised
str18 = "I'm a good boy"
print(str18) #it prints the normal string given above but if we want to replace anything we jst do like given below 
print(str18.replace("good","bad")) #it replaces all the occurences of the old ones to the new ones,for here the word 'good' will be exchanged wid 'bad' doesn't matter how many times used in sentence  
print(str18.replace("o","z")) #it will replcace all the 'o's from the given string to 'z' 
print(str18.find("o")) #it will print the exact position of the given word or alphabet , if it's more than once it'll basically show the 1st position in the string
print(str18.find("good")) #it will print the position where "good" started (NOTE:DON'T FORGET THAT POSITION/INDEX IN PYTHON STARTS FROM 0 THEN 1,2,3... N ALL)
print(str18.find("bad"))  #like here if you try to find the position of a word/alphabet which is not in thhe given string it'll just show the position '-1' cause as such koi position define nahi hai until if we talk bout slicing
str19 = "I'm more more more not into much sports"
print(str19.count("more")) #it will print the number of times the word/alphabet has been repeated in the string
print(str19.count("o")) #as above we saw that bout the whole word now it'll show ki how many times the given word is repeated or present in the given string 
 
 #let's practice
 #1.Write a program to input user's first name and print it's length.
name1 = input("enter first name: " ,)
print("length of your name is ",len(name1))
 #2.WAP to get the occurence of $ in a string.
str20 = "I'm just $$$ me $$ ngll"
print(str20.count("$")) 

#conditional statement(these statements act as a decision-making tool that direct the execution flow of a program)
#syntax: if-elif-else
  #1> if
  #example
age = 4 #here age is 4 which obv is less than 21 so the output will be a defined for that you can change the age and see by yourself 
if(age >= 21):
    print("can have child") #notice the extra space we gave or by simply using 'tab' key once for conditional statements it's called "Indentation"  
    print("can consume alcohol")
    print("obv can drive too")
    print("should def do something to earn ngl if unemployed") #as you can see these statements will get printed if the conditions are satisfied and if it's not satisfied then the following code will do the job 
else:
    print("too young kiddo,go play with toy cars..") #if we haven't given this code , python would've shown no output like as if it never existed when the condition isn't satisfied 
    
  #2> elif(shorty of else if) 
  #example
light = "yellow" #light is yellow so the output will be as defined for the color yellow 
if(light == "red"):
    print("stop!!!")
elif(light == "green"):
    print("go!!") 
elif(light == "yellow"):
    print("get ready to go") 
  # "elif" or "if" we can use as many as we want in the code but the only condition is if we're using 'elif' there must be atleast one 'if' statement before but there's no such thing for 'if' we can use it from starting to end,and remember that agar saare 'if' wale statement FALSE hue toh hi jaake 'elif' wale statement check hoga but if shuru wala 'if' statement hi TRUE hogya toh obv 'elif' aur check bhi nahi hoga
  #NOTE: basically simplified 'elif' is dependent on 'if' but the vice versa isn't true.
  #another some examples to show the difference b/w 'if' & 'elif'
#(I):-
num21 = 3
if(num21 > 2):
    print ("Yeah it's greater than 2 you dummo")
if(num21 > 1):
    print("idk") #here you'll get 2 outputs cause both the statements are TRUE.
#(II):-
num22 = 5
if(num22 >= 5):
    print("yuppies")
if(num22 < 3):
    print("this statement will not get printed cause this is FALSE")
#(III):-
num23 = 7
elif(num23 > 8):
    print("nope")
elif(num23 = 7):
    print("yeah") #this will show error cause again it's literally 'ELSE IF' , there's no significance of it without 'IF' before itt...



#3> 'ELSE' statement - 
#if all the statements above doesn't matters 'IF' , 'ELIF' all are false then we use 'ELSE'.
#example given as
stoplight = "blue"
if(stoplight == "red"):
    print("STOP!!")
elif(stoplight == "yellow"):
    print("GET READY")
elif(stoplight == "green"):
    print("GO")
else:
    print("THE STOPLIGHT IS SHADYYY NGL...")

##question- Grade student based on marks ,which are given as
#marks>=90 => grade = A 
#marks<90 but marks>=80 => grade = B 
#marks<80 but marks>=70 => grade = C 
#marks<70 => grade = D
marks2 = int(input("enter student marks: ")) 
if(marks2 >= 90 ):
    grade = "A"
elif(marks2 < 90 and marks2>= 80 ):
    grade = "B"
elif(marks2 < 80 and marks2 >= 70 ):
    grade = "C"
else:
    grade = "D"
print("grade of the student--> " , grade)

#NESTING(The practice of placing one programming structure inside another , relying on strict indentation to define the heirarchy) or (aise keh sakte hain ki ek statement ke andar aur ek statement likhna)

age = 33
if(age >= 18):
    if(age >= 90):
        print("can't drive")
    else:
        print("can drive")
else:
    print("cannot drive")

#LET'S PRACTICE:-
#Q.1> WAP to check if a number entered by the user is odd or even.
 
a1 = int(input("enter the number: ")) 
b1 = 2 
c1 = a1 % b1
if(c1 == 0 ):
    print("Given number is EVEN")
else:
    print("Given number is ODD")

#Q.2> WAP to find the greatest of 3 numbers entered by the user .
 
a2 = int(input("enter 1st number: "))
b2 = int(input("enter 2nd number: ")) 
c2 = int(input("enter 3rd number: ")) 
if(a2 > b2 > c2):
    print(a2 , "is the greatest among given")
elif(a2 > c2 > b2):
    print(a2 , "is the greatest among given")
elif(b2 > a2 > c2):
    print(b2 , "is the greatest among given")
elif(b2 > c2 > a2):
    print(b2 , "is the greatest among given")
elif(c2 > a2 > b2):
    print(c2 , "is the greatest among given") 
elif(c2 > b2 > a2):
    print(c2 , "is the greatest among given")
elif( a2 = b2 = c2):
    

    
    


    








   















