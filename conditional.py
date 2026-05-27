# function input(), print(), int()

number = int(input())  #  int( input() ) =>  int(2) # 2 /// name ==> int("name") => ValueError
print(number)


# if we need to input  string, then only input() can be used
# If we need to input an integer number like 1, 2, -100, 10. etc, we need to use int(input())
# if we want to input a float number like 3.14, -1.22, 1.00, we need to use float(input())


if number > 10:
    print("The number is greater than 10")

elif number == 10:
    print("The number is 10")
else:
    print("The number is not greater than 10")


# Whether the entered number is divisible by 2 and 5

if number % 2 == 0 and number % 5 == 0:
    print("The number is divisible by 2 and 5")

elif number % 2 == 0:
    print("The number is divisible by 2")

elif number % 5 == 0:
    print("The number is divisible by 5")

else:
    print("The number is not divisible by 2 and 5")

#### Modulas operation
# 4 / 2 = 2, remainder = 0
# 5 / 2 = 2, remainder = 1
# 10 / 5 = 2, remainder = 0
# 11 / 5 = 2, remainder = 1