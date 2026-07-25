#DICTIONARY IN PYTHON 
#>Dictionaries are used to store data values in key:value pairs . 
#>They are unordered , mutable(changeable) , & don't allow duplicate keys . 
#ex.1>
info1 = { 
    "key" : "value",
    "name" : "Madhusudan",
    "age" : 19,
    "is_adult" : True ,
    "marks" : 94.4 
}
print(info1)
#NOTE : In list every class of value is acceptable like int,float,string,list,tuple,etc.
#ex.2>
info2 = { 
    "key" : "value",
    "subjects" : ["python","java","C++"] ,
    "topics" : ("dictionaries","set") ,
    "marks" : 94.4 
}
print(info2)
print(type(info2)) #This will say ki it's class is 'DICT'

#NOTE: You can't use LIST & DICTIONARIES inside key .
# As we earlier are used to to a thing called index which was there in list and tuple but there's no such thing as index in dictionaries .
# But if we wanna have a particular value we can just print it by it's key . 
#  Syntax - print(dict["key"])
#ex.3>
print(info2["subjects"]) #output-['python','java','C++']
print(info1["name"])#output-Madhusudan
print(info2["topics"])#output-('dictionaries','set')
#NOTE: If we try to get output of a key which doesn't exist it'll show error ki that particular key isn't present in the dictionary & it'll show "KeyError:'key'".
#If we wanna assign a new value to a key then that's also possible (Syntax : dict["key"] = "new value" or 00{if there's a number no need put it in double quotation mark}) as given in the example below .
#ex.4>
info3 = {
    "name" : "Tyler",
    "Age" : 25,
    "School" : "DCE" 
}
info3["Age"] = 26  #here we jst changed the value of the key 'Age' .
info3["Class Teacher"] = "Priya Ma'am" #here we can add a new key too by using the same syntax .
print(info3) #It'll print the dictionary with the new value of 'Age' .
#NOTE : If we try to assign a NEW KEY with the SAME NAME but different VALUE as last then it won't create a new key instead it'll overwrite the value that's why in above example we're able to change the value of a particular key .
#NULL DICTIONARY (this is the empty dictionary but later on you can obv add keys n values as seen by examples above )
#ex.5>
null_dict = {}
print(type(null_dict)) #it'll obv say tht it's from DICTIONARY class
print(null_dict) 
null_dict["name"] = "CAT"
print(null_dict) #this'll print the updated(new data added) dictionary.
#NESTED DICTIONARY 
student1 = {
    "name" : "yadav kumar" , 
    "subjects" :{
        "phy" : 94 ,
        "chem" : 89 ,
        "math" : 99 ,
        "eng" : 86
    }
}
#this is how NESTING works here too .
print(student1) #this'll print the dictionary 'student1' 
print(student1["subjects"]["math"]) #this'll precisely print the value of 'math' from 'subjects' from 'student1'..I mean yeah 'subjects' also became a dictionary .

#DICTIONARY METHODS
#I> Syntax - print(dict.keys()) --> returns all keys
#ex.6> 
print(student1.keys()) #this'll print all outer layered keys which means this won't be printing NESTED Keys .
# We can also type cast the dictionary into anything else like in the below example we'll make it a list .
print(list(student1)) 
#        OR
print(list(student1.keys())) #it'll print it as a list .
# If we want to find the no. of keys in the dictionary we can either try to print the length of dictionary or we can also print the length of the list we created for the keys .
print(len(student1))
#      OR
print(len(list(student1)))  
#II> Syntax - print(dict.values()) --> returns all values
print(student1.values()) 
#         OR
print(list(student1.values())) #from here we can also see that one DATA-TYPE can also be stored in another data type like here in the output of this code we can say dictionary is stored in list .
#III> Syntax - print(dict.items()) - returns all (key,value) pair as a tuples .
print(student1.items()) 
#         OR
print(list(student1.items())) 
#if we want to access the tuples individually then we can go like thiss
pairs = list(student1.items()) 
print(pairs[0]) #this'll print the 0th tuple 
#IV> Syntax - print(dict.get("key")) --> returns the key according to value .
print(student1.get("name"))
#         OR
print(student1["name"]) #both code will give the same result but if you try to print value of a key that doesn't exist you'll see the difference i.e given below the example .
#ex.7>
# print(student1["name2"]) --> this'll show error but the other one won't , i.e
print(student1.get("name2")) #this'll show no error in that place it'll just show 'NONE' , which again beneficial while coding for a big task cause after ERROR no output is shown .
#V> Syntax - dict.update({"key":"value"}) --> updates the keys & values in the dictionary 
#ex.8>
student1.update({"city":"BBSR","age" : "19"})
print(student1)
#              OR
new_dict = {"lang":"javascript"}
student1.update(new_dict) #we just made a new dictionary & as we used this program this new dictionary is added to the old dictionary and the old one got updated .
print(student1) #this'll print the updated dictionary .
#NOTE : In dictionaries , duplicate keys aren't allowed so if we use the same KEY which is already used in the old dictionary but with a new VALUE it'll just update the value of that particular KEY .
#ex.8>
student1.update({"city":"BBSR","age" : "20"})
print(student1) #it'll print the updated dictionary 

# SETS IN PYTHON - Set is the collection of un-ordered items , each elements in the set must be unique & immutable . 
# We can put any immutable thing like int , tuple , boolian , string , float ,etc in SETs but not the mutable ones like list , dictionaries ,etc.
#ex.9>
collection1 = {1,2,3,4,"cat","dog"}
print(type(collection1)) #this'll print it as <class 'set'>
print(collection1)
#ex.10>
collection2 = {6,7,7,8,6,6,"cat","cat","cat"} 
print(collection2) # altho it'll print but you can see as it is UNORDERED like might be something coming before something  but jst not acc to the above & the duplicate items are also removed in the output .
print(len(collection2)) # this'll print total number of items in the output .
# If we want to make a EMPTY SET , then :
collection3 = {}
print(collection3)
print(type(collection3)) #this won't work cause it'll print it as dictonary AKA EMPTY DICTIONARY , but if we use the syntax given below....
collection4 = set() 
print(collection4)
print(type(collection4)) #now this'll print as SET AKA EMPTY SET .

#NOTE : SET is MUTABLE but the elements inside it is IMMUTABLE 
# SET METHODS 
#I> syntax - set.add(element) --> adds the element 
#ex.11>
collection5 = set()
collection5.add(1)
collection5.add(2)
collection5.add(2) # this obv will not get printed cause it's the duplicate one na . 
collection5.add((1,2,3)) #we also can add TUPLE but not LIST as that is mutable & it'll show "TypeError : unhashable type : 'list'" .
print(collection5) #output - {1,2}
#II> syntax - set.remove(element) --> removes the element 
collection5.remove(1) #this will remove the element "1" .
print(collection5) 
#NOTE : If we try to remove something which isn't there in the set then it'll show "KeyError" .
#III>syntax - set.clear() --> empties the set 
#ex.12>
collection6 = set()
collection6.add(2)
collection6.add(3)
collection6.add((1,5,7))
print(collection6)
collection6.clear()
print(collection6) #this gonna print the empty set
#IV> syntax - set.pop() --> removes a random value 
#ex.13>
collection7 = {"rock","classic","pop","jazz"}
collection7.pop()
print(collection7) 
#V> syntax - setX.union(setY) --> combines both set values & returns new (same as mathematical operation known as UNION )
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2)) #just as the mathematical opreration of UNION it will just give the output i.e the UNION of those sets .
#NOTE : Even after UNION operation , we still can print the value of set1 & set2 respectively , i.e 
print(set1)
print(set2) # yep these will print those respectively .
#VI> syntax - setX.intersection(setY) --> combines common values & returns new (same as mathematical operation known as INTERSECTION)
set3 = {1,3,5,7}
set4 = {5,7,9,11}
print(set3.intersection(set4)) #this'll print the intersection between two sets .

#LET'S PRACTICE 
#Q.1> Store following word meanings in a python dictonary :
# table : "a piece of furniture" , "lists of facts & figures"
# cat : "a small animal"
dict1 = { 
    "table" : ["a piece of furniture" , "lists of facts & figures"] ,
    "cat" : "a small n lovely animal"
}
print(dict1)
#Q.2> You're given a list of subjects for students . Assume one classroom is required for one subject . How many classrooms are needed for one student ? 
#   'python','java','C++','python','javascript','java','python','java','C++','C'.
subjects1 = {"python","java","C++","python","javascript","java","python","java","C++","C"} #we jst made a set of it and when we'll print the set it'll give the unique values 
print(subjects1) #here it gave the unique ones and if we wanna know bout the number of classrooms we can jst print the length of the set
print(len(subjects1)) #it'll be the answer of the question asked .
#Q.3> WAP to enter marks of 3 subjects from the user & store them in the dictionary . Start with an empty dictionary & add one by one . Use subject name as KEY & marks as VALUE .
dict2 = {}
subject1 = input("enter 1st subject : ")
subject2 = input("enter 2nd subject : ")
subject3 = input("enter 3rd subject : ")
marks1 = int(input("enter marks subject1 : "))
marks2 = int(input("enter marks subject2 : "))
marks3 = int(input("enter marks subject3 : ")) 
dict2 = {
    subject1 : marks1 ,
    subject2 : marks2 ,
    subject3 : marks3 
}
print(dict2)
print(type(dict2))
#Q.4> Figure out a way to store 9 & 9.0 as separate values in the set . (You can take the help of built-in data types)
set5 = {"9",9.0}
print(set5)













































    