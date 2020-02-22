""""
Working with python
lists and dictionaries
"""
#defining a list
fruits =["apple","mango","orange","lemon"]
#checking the type
print(type(fruits))
print(fruits)
 #modifying a alist
 #adding new items to an existing list
fruits.append("Water melon")
print(fruits)
#adding to a specified position.
fruits.insert(1,"avocado")
print(fruits)

#removing items in a list
fruits.remove("apple")
print(fruits)
#removing items by specifying their index
# position
fruits.pop(2)
print(fruits)

#to clear your list we use
# clear() function
print(len(fruits))
fruits.clear()
print(fruits)
print('the length of our fruits list')
print(len(fruits))

newlist =[1,2,3,"number 4", "number5"]
print(newlist)
print(type(newlist))

""""
Working with Dictionaries
"""
#dict is a key value ,apping.
#for example orange and their amount
inventory ={"orange":200,"apple":300,
            "lemons":100}
print(type(inventory))

phone_book = {"Brom":718989,"Keva":25466,
              "joyleen":2547777}
print(type(phone_book))
months= {1:"Jan", 2:"FEb", 3:"March"}
relatives={"cousin":"Jack ",
           "Brother":"John",
           "Sister":"Joy"}
print('the type is: ',type(relatives))
print(relatives)
relatives["cousin"] = "Jackson Mwirigi"
print(relatives)
#creating a copy of relatives
copy = relatives.copy()
print('This is a copy',copy)
copy["Brother"] ="Jacob"
print(relatives)
print(copy)

""""
Working with IF Statements
"""

#we use if statements to check if an
# expression is true or false.
#if true we do something.

# age= int(input("enter your age"))
#
# if age>=18:
#     print("You are an adult")
# else:
#     print('You are not an adult')

# user_int = int(input("enter any number"))
# if user_int <0:
#     print("This is a negative number")
# else:
#     print("This is a positive number")


"""
Working with for loop
"""
# we use for loop to iterate through
#character sectuence or arithemetic / numbers


numbers = [1,2,3,10,11,12,14,20]
print(numbers)

for number in numbers:
    print('item exists', number)
name= "Jackson Mwirigi"
for letter in name:
    print(" letter ",letter)
fruits1=['orenge', 'lemon', 'apple']
for item in fruits1:
    print("item " , item)
#the range function generates a sequence
# of numbers from  0 to the
# specified last digit
for number in range(12,20):
    print(number)
"""
Working with While loop in python
"""
#with while loop we do
# something as long as the expression
# remains true,
# we break./stop the loop when false

new_age= 0
# while new_age< 18:
#     print('you are under eighteen')
#     new_age +=1
#
# a = 0
# while a<4:
#     print(a)
#     a +=1
# limit= 3
# count = 0
# name= "MYNAME"
# while count<limit:
#     guess=input("enter guess name").upper()
#     count +=1
#     if guess == name:
#         print('correct guess')
#         break
#     else:
#         print('wrong guess')

# print(name.upper())
#
# guess= input("enet name").upper()
# print(guess)

if (20<10) and (30<50) :
    print("all less than 50")
else:
    print('all are above 50')

