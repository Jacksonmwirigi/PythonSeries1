
#to create an object in python we need classes.
#we define a class using the class keyword

#an object has attributes and proceduces/methods of interacting with it.
#a class is a blueprint of an object.
#lets define our first python class.

class className:
    #statements
    pass

#lets create person object
class Person:
    #person has attributes like name, age, gender
    pass

#create an instance of an object
#to creat a person object we do as below
person = Person()
#assigning attributes to an object
person.name = 'myname'
person.age = 20
person.gender= 'male'
print(person)
print(person.gender)
print(person.age)


class Employee:
    def __init__(self, name,age, gender, company):
        #self refers to a particular instance of a object.
        self.name = name
        self.age = age
        self.gender = gender
        self.company = company

    def print_employee_profile(self):
        print('employee name is ', self.name, 'age is',
              self.age, 'company ', self.company)

employee1= Employee("Jack",20,'male', "modcom")
# print(employee1.gender)
# print(employee1.name)
#
employee2 = Employee('Brom', 20, 'male', "copmanyxyz")
#accessing the employee_profile function/method
employee1.print_employee_profile()
employee2.print_employee_profile()








