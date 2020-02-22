""""
PYTHON CLASSES(student Assignment)
"""
#Instructions available on the link below
#https://justpaste.it/5twyp

dept = 0
class Employee:
    def __init__(self, employee_name, gross_income, number_of_children):
        self.employee_name = employee_name
        self.gross_income = gross_income
        self.number_of_children = number_of_children
        # self.net_income=net_income

    def dependency_exemption(self):
        dependency_exemption = 3000 * self.number_of_children
        dept = dependency_exemption
        return dept
        # dept dependency_exemption
        # print('dependency_exemption=', dependency_exemption)

    def net_income(self):
        # print("dep=",dependency_exemption())
        # _empName=input('Enter Name:')
        # dep = self.dependency_exemption(self)

        net_income = int(self.gross_income) - dept
        # _net_income=net_income
        #dependency_exmption = int(3000 * self.number_of_children)
        print('Gross income=', self.gross_income)
        print('Dependency_exmption=', dept)
        print('Net Income=', net_income)
        if (net_income > 0 and net_income <= 50000):
            tax_due = net_income * 0.15
            print('Tax Due=', tax_due)
        if (net_income > 50000):
            tax_due = 50000 * 0.15 + ((net_income - 50000) * 0.25)
            print('Tax due=', tax_due)

    # def tax_due(self):
    # if(net_income<=50000):
    #   tax_due=net_inome*0.15
    # print ('Tax due=',tax_due)
    # if(net_income>50000):
    # tax_due=50000*0.15+ (int(net_income)-50000)*0.25
    # print ('Tax due=',tax_due)

_number_of_children = int(input("Enter number of children:"))
_gross_income = int(input("Enter your gross salary:"))
_employee_name = input('Enter your Full Name: ')
Employee1 = Employee(_employee_name, _gross_income, _number_of_children)
Employee1.dependency_exemption()
Employee1.net_income()
# Employee1.tax_due()


# # to create a an employee class constructed using employee_name, gross_income, and number of children as its attributes.
# class Employee:
#     def __init__(self, employee_name, gross_income, number_of_children):
#         self.name= employee_name
#         self.gross_income = gross_income
#         self.number_of_children = number_of_children
#
#     def compute_due_tax(self):
#         dependency_exemption =3000 * self.number_of_children
#         net_income= self.gross_income - dependency_exemption
#         # return  net_income
#         if  net_income>0 and  net_income <=50000:
#             tax_due= net_income* 0.15
#             return tax_due
#         elif net_income>50000:
#             tax_due= net_income*.15
#             return tax_due
#
# employee1 = Employee(number_of_children= int(input('Enter number of children ')),employee_name= input('Enter employee name '),
#                      gross_income= float(input('Enter the Gross Income ')))
# print(employee1.name)
# print(employee1.compute_due_tax())