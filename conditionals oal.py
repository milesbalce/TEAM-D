# Condition operators in python <, >, <=, >=, == (equal), != (not equal)
# print(3 >= 3)
# print(3 <= 3) #will still show true even if sign of < is changed. 
# print(3 == 3) 
# print(3 != 3) # != not equal to
# true and false are known as boolea in coding, value of 1 assumes true and value of 0 assumes false
# print("a" < "b") #true because of the alphebetical order as a is a lower oder than b.

# set_pw = "tgif"
# print(set_pw == "tgip")
# print(set_pw <= "tgip") #p would have a higher alphabetical order than f thats why python evaluate this condition as true.


# Comparison operators in python: <, >, <=, >=, == (equal), != (not equal)
# Logical operators: and, or, not


# num1 = 200
# print(num1 > 150 and num1 < 250) # return and evaluation of true the and operator will require both left and right to return true to evaluate an overall true.
# num2 = 300
# print(num2 > 150 and num2 < 250)
# print(num2 > 150 or num2 < 250) #only required one to return true

# print(not True)
# print(not False)

# print(not False == 1)

# if and else statement
# language = "python"

# if language == "python":
#     print(f'Programming language is {language}')

# if language != "python":
#      print(f'Programming language is {language}') #output does not output anything

# singtel = 1.3
# starhub = 1.8

# if singtel > starhub:
#     print("Singtel price is higher than Starhub")
# else:
#     print("Starhub price is higher than singtel") #will not print it bcos not true CONDITIONSS!!!

# singtel = 2
# starhub = 1.8

# if singtel > starhub:
#     print("Singtel price is higher than Starhub") #will not b printed
# else:
#     print("Starhub price is higher than singtel")


# elif keyword (else if, all conditions included)
#3 conditions for this scenario as they can be greater then less than and equal

# singtel = 1.8
# starhub = 1.8

# if singtel > starhub:
#     print("Singtel price is higher than Starhub") 
# elif singtel < starhub:
#     print("Starhub price is higher than singtel")
# elif singtel == starhub:
#     print("Share price are equal") #will be evaluated as true and thus will show on output



# Conditions and loops (are often used hand and hand to control the flow in an iteration)
# even_sum = 0
# odd_sum = 0

# for num in range (10):
#     if num % 2 == 0:
#         even_sum += num
#     else: odd_sum += num 

# print(f'Even sum of 1 to 10 = {even_sum}')
# print(f'Odd sum of 1 to 10 = {odd_sum}')


# break keyword (to stop an iteration when certain conditions are met)
# range_value = range(50,100)

# for index, num in enumerate(range_value):
#     print(index, num)
#     if index == 5:
#         break #used to fine tune the control flow of a program better

# for index, num in enumerate(range_value):
#     print(index, num)


# continue keyword (to skip iteration)
# for num in range(10):
#     if num == 5 or num == 6:
#         continue
#     print(num) #printed due to the execution of continue keyword


# price1 = 68
# price2 = 58

# if price1 != price2:
#     print('Not equal')
# else:
#     print('Equal')

# sum = 0 
# for num in range(7):
#     sum += num
#     if num == 4: 
#         break 
# print(sum)

sales = 7000
manager = False

if sales >= 5000 and not manager:
    print('15% commision')
elif sales >= 5000 and manager:
    print("10% commision")
else:
    print("no commision")

# high_pressure = False

# if high_pressure:
#     print("You have high blood pressure")
# else:
#     print("You do not have high blood pressure")