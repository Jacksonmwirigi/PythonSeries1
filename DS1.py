import pandas as pd

import matplotlib.pyplot as plt

#create a dataframe
#reading the csv file
dataframe = pd.read_csv('school.csv')
# print(dataframe)
#read the first 10 rows
#print(dataframe.head(10))

#read the last 10 rows
# print(dataframe.tail(10))

#to see statistics of our data we use describe function
# print(dataframe.describe())

#checking for empties
# print(dataframe.isnull().sum())

#cleaing our data
#filling the empties
# print(dataframe['bday'])
# print(dataframe.bday)

dataframe['bday'].fillna('unknown', inplace=True)
#inplace keyword means apply changes
# print(dataframe.isnull().sum())
#printing the first 20 rows for the bday column
# print(dataframe['bday'].tail(20))

dataframe['Gender'].fillna(3, inplace = True)
# print(dataframe.isnull().sum())
# print(dataframe.Gender.head(40))


#replacing categorical data labels
print(dataframe.Gender)
dataframe['Gender'].replace(0, 'Male', inplace= True)
dataframe.Gender.replace(1, 'Female', inplace = True)
dataframe.Gender.replace(3, 'Unknown', inplace= True)
print(dataframe.tail(10))

#visualisation
fig, ax = plt.subplots()
ax.hist(dataframe['English'], bins=20)
plt.xlabel('english')
ax.x_label('Test')
plt.show()