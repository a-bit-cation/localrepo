#LISTS IN PYTHON - A built-in data type that stores set of values.
#It can store elements of different types(integer,float,string,etc)
#ex.1>
marks = [97.8,94,56,74,33,89,86,80,82]#if we want to make a list then we've to use these square brackets,and put the list in it like shown here .
print(marks)#this will print the list we've given above .
print(type(marks))#this will print the type of that which is 'LIST'.

#NOTE:There are some similarity between string and list such as index which means position of the data in the list,which also starts from 0 to.....depending upon how much data you put in that
#ex.2>(index in list)
print(marks[0]) or print(marks[2]) or print(marks[5]) or print(marks[8]) #we already know by math that "OR" means 'Union', so yeah basically it will print the data present in the position i've given(btw it's not in lecture cause you found it by yourself)
#NOTE:One major difference b/w string and list is that string is IMMUTABLE while list is MUTABLE(which means changes can be done after assigning a list but for string it's not possible)
#ex.3>(strings are immutable)
str1 = "rahul"
print(str1[0])
str[0] = "f"


