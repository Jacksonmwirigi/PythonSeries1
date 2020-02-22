#This is a comment.

"""
This is a
multi-line
comment
"""
name = "jackson "
print(type(name))
age= 20
print(type(age))
balance = 1000.20
print(type(balance))

#arithmetic operations
#addition.
numb1= 20
numb2 =10

result = numb1+ numb2
print("the result is: ")
print(result)

#division we use /
#multiplication we use *
#substraction -

height= 1.2
weight= 80
bmi= weight/(height*height)

print(bmi)

#multiply a by c
a= 2
c= 7
d= a*c
print(d)
r= 3
p= 10000
time =3
si = 0.03*p+time

myname = "Jackson"
myfriend= "Tob"
print(myfriend, "is ", myname,"'s friend"   )

print("Simple interest will be {}".format(si))

""""
inbuilt python 
functions

"""
#checking length of characters in a string
#we use len() function
school_name ="modcom institute"
print("The length of school name variable is ",len(school_name))


#returning an integer from a float variable
acc_balance = 200.50
print(acc_balance)
print(int(acc_balance))
print(school_name.capitalize())

print(type(age))
print(type(str(age)))
print("acc data type")
print(type(int(acc_balance)))


eng =90
sci=75
math=80
mean =(eng+sci+math)/3
print(mean)

#Defining list in python
student_names= ["Tob", "Fred", "Joylene", "Brom"]
print(type(student_names))

print(len(student_names))

student_regnumbers= {"name":'Tob', "phone":'0977'}
print(type(student_regnumbers))

cars= {"model_number":'ToyotaXX',
       "Number plate":'KCW99',"price range":'2000-288838'}
print(cars)
school_name= "modcom institute"
print(school_name)
print(school_name[-2])
print(student_names[2])


new_age= 18
if(new_age<18):
    print("Not eligible to apply for an ID")

else:
    print("eligible for an ID")

#to prompt for user input we use
#input() function


user_age =int(input("provide your age"))
print(user_age)
print(type(user_age))

if(user_age<18):
    print("Not an adult")
else:
    print("You are an adult")

