"""
Functions in Python.
"""
#we define a function
# using the def keyword

def hello_world():
    print('Hello world')

# hello_world()
#
# def addition():
#     a=3
#     b=5
#     print(a+b)
#
# addition()
#
# #simple interest
# def calculate_simple_interest():
#     rate = 3
#     time = 2
#     principle = 60000
#     simple_interest = rate*time*principle/100
#     print('simple interest is',simple_interest)
#
#
# calculate_simple_interest()
#
# #bmi = weight/height*height
#
# #working with functions that has arguments
# def calculator (num1, num2):
#     print(num1+num2)
# calculator(10.0,30)
#
# def welcome_message(name, friend_name):
#     # name = input('provide your name')
#     print('Welcome ',name)
#     print("Hello Mr {} Nice "
#           "to meet you {}"
#           .format(name, friend_name))
#
# name = input('provide your name')
# friend_name = input('Enter friend\'s name')
# welcome_message(name,friend_name)


#Return Type
def division(number1, number2):
    answer = number2/number1
    return answer

# num1= float(input('enter a number'))
# numb2 = float(input('enter number 2'))
# print(division(num1, numb2))
return_value = division(20,100)
print(return_value)
print(return_value +40)


#Task 1
# We have two monkeys, a and b,
# and the parameters
# a_smile and b_smile indicate
# if each is smiling.
# We are in trouble if they are both smiling
# or if neither of them is smiling.
#  Return True if we are in trouble.


def students_marks (*marks):
    print(marks)
students_marks(70, 60,40)
def students_subjects(**marks):
    return marks
students_marks()
subjects =students_subjects(English=80,
                                  Maths = 60,
                      Swahili =87)
print(subjects)
for key, value in subjects.items():
    print('keyword', key, 'its value', value)
