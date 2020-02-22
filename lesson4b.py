
# Write a Python class named Circle constructed by a radius and
# two methods which will compute the area and the perimeter of a circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        area = 3.142 * self.radius * self.radius
        print(area)
    def calculate_perimeter(self):
        perimeter = 3.142 * 2*self.radius
        print(perimeter)
circle1 = Circle(14)
circle1.calculate_area()
circle1.calculate_perimeter()

#inheritance
class SubCircle(Circle):
    pass
subcircle = SubCircle(6)
subcircle.calculate_perimeter()

#create a class Names constructed using word
#create two methods that displays the provided
# word and another one that prints word length.






#create a class Employee constructed using salary,
# allowance and employee_name
#implement two methods to compute the
# employee's gross income and print their

#for data science.
# pandas  #for data preparation and clean up
# matplotlib, seaborn  #for data visualisation.
# numpy # for working with numbers

#for ML
#we do sklearn for machine learning algorithms


