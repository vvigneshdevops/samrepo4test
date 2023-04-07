## Join --  "".join(list) can be used to join elements of a list (or another iterable such as, tuples or dictionaries). Joining character goes inside the brackets and list goes inside the parenthesis. 
#Syntax:   "".join(list). Returns the joined element
emailadd=("Mr.Hathaway", "amymail.com")
res="@".join(emailadd)
# print(res)  #Mr.Hathaway@amymail.com

##Split -- .split() method can be used to split strings based on a given character. It returns a list of split substrings.
# Syntax: .split(" ")
str="101:102:103:201:202"
lst=str.split(":")
# print(lst)  #['101', '102', '103', '201', '202']

##Strip : .strip() method will strip specified character(s) from the string it’s applied to. We have lstrip(); rstrip()
s= " Hi There  "
str=s.rstrip()
# print(str)

##Lambda : Anonymous function ; Returns the processed result
# Syntax : res= lambda value:expression

val=lambda x:x*2
# print(val(2))  # 4
l=[221,172,103,201,202]
# r=sorted(l, reverse=True)
# l.sort() # Sort in asc order  [103, 172, 201, 202, 221]
# l.sort(reverse=True) # Sort in reverse order[221, 202, 201, 172, 103]

#Using Lambda
#  l.sort(key=lambda x:x)
# print(l) #[103, 172, 201, 202, 221]

#sorted() is not a method but a builtin function. It’s main difference from .sort() method is that it won’t change the original list it will simply output a new list. 
lst = [1, 5, 66, 7]
# re=sorted(lst, key=lambda x:x)  #[1, 5, 7, 66]
res=sorted(lst, key= lambda x:x, reverse=True)  #[66, 7, 5, 1]
# print(res)

## Zip module
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
points=dict(zip(lst1,lst2))
# print(points)  # {'Netflix': 198, 'Hulu': 166, 'Sling': 237, 'Hbo': 125}

## map() function takes two arguments, first the function, then comma and second the name of the list to be used for the mapping function.
# Syntax : map(function, list)
lst2=[198, 166, 237, 125]
mapres=map(lambda x:x+5, lst2)
# print(list(mapres))  # [203, 171, 242, 130]

## filter  filter function are usually logical expressions since the list will be filtered based on this logic.

filtres=filter(lambda x:x%2==0, lst2)
# print(list(filtres)) #[198, 166]

'''Syntax of List Comprehension in Python
mylist = [output/expression for item in iterable if condition == True]
List comprehension mainly has three components:
    For loop: It is mandatory and loops over the given iterable.
    Condition and expression: It is optional and is used to imply some condition over the iterable
    Output: It is mandatory and the variable(or expression) we provide as output is added to our list.
'''
l=[1,5,6,7,8,9,10,11,12]
# res=[i for i in l if i%2!=0]

#squaring the value of output we get
res=[i**2 for i in l if i%2==0]
# print(res)


#Write a reg expression that confirms an email id using the python reg expression module “re”
import re
# print(re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","55micheal.pages@mp.com"))

def main():
    print("Checking main functon\n")

    if '__name__' == '__main__':
        main()
