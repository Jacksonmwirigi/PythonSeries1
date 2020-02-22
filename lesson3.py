
number_list = []
for number in range(1500,2701):
    if number %7==0 and number%5==0:
        number_list.append(number)
print(number_list)

# word = "SWAHILI DISHES"
# for letter in word :
#     print(letter)
# "YOUR NAME IS ", NAME
#print the above 3 times.

#task 3
# # Problem:  come up with
# a multiplicaiton table of 5,
# that produces like below
# # 1 * 5 = 5
# # 2 * 5 = 10
# # 3 * 5 = 15
# # 4 * 5 = 20
# # 5 * 5 = 25
# # 6 * 5 = 30

num = 5
for number1 in range (0,7):
    print(number1, "*", num,
          "=",number1*num)


i = 0
print('starting the while loop')
while i<=6:
    print(i,"*",num,"=",i*num)
    i+=1