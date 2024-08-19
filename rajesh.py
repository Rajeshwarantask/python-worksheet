name = input("what is your name??\n")
print("Hello " + name + " ,\nThank you so much for using my calculator.\n")
menu = "ADD(+), SUBRACT(-), DIVIDE(%),MULTIPLY(*)."
print(name + ",What would you like from our Calculator today?\n\nHere is what we are doing.\n\n" + menu)
order = input("what do you want to do???\n")
if order == "add":
     price = input("The number what you want to ADD?\n" )
     quantity = input("The number what you want to ADD with previous number?\n")
     total = int(price) + int(quantity)
     print(str(total))
elif order == "subract":
    price = input("The number what you want to SUBRACT?\n" )
    quantity = input("The number what you want to SUBRACT with previous number?\n")
    total = int(price) - int(quantity)
    print(str(total))
elif order == "divide":
    price = input("The number what you want to DIVIDE?\n" )
    quantity = input("The number what you want to DIVIDE with previous number?\n")
    total = int(price) / int(quantity)
    print(str(total))
elif order == "multiply":
    price = input("The number what you want to MULTIPLY?\n" )
    quantity = input("The number what you want to MULTIPLY with previous number?\n")
    total = int(price) * int(quantity)
    print("your total is " + str(total))
else:
    print("sorry "+ name +" we can't find what you are trying to do!!")


# 2.PYTHON CODE FOR WEIGHT AND CALORIES CALCULATOR

name = input("what is yours name??\n")
print("Hello " + name.upper() + "!!\nNow,Any weights can be calaculated.\nBecause of intelligence i'll improve more than this next time!!\n")
order = input("what is yours weight??\n")
if order == (order):
    price = 2.20462
else:
    print("sorry, we can't find that here. ")
total = price * int(order)
print("Thank you so much for measuring.\nHave a good day.\nYour total is: Pounds =" + str(total))
print("Done by RAJESH")

order = input("The number what you want to SUBRACT?\n" )
if order == (order):
    quantity  = input("The number what you want to SUBRACT with previous number?\n")
    total_ = int(order) - int(quantity)
    print(str(total_))
    calories = 7716.179176
    total_calories = int(calories) * int(total_)
    print(name.upper() + " Thank you for measuring.\nYou must burn these calories = " + str(total_calories) +" kcal. ")
else:
    print("Thank you for visiting. ")



# 3.PYTHON CODE FOR WEIGHT CALCULATORT

name = input("what is yours name??\n")
print("Hello " + name.upper() + "!!\nNow,Any weights can be calaculated.\nBecause of intelligence i'll improve more than this next time!!\n")
order = input("what is yours weight??\n")
if order == (order):
    price = 2.20462
else:
    print("sorry, we can't find that here. ")
total = price * int(order)
print("Thank you so much for measuring.\nHave a good day.\nYour total is: Pounds =" + str(total))
print("Done by RAJESH")



# 4.PYTHON CODE FOR AGE CALCULATOR

name = input("what is your name??\n")
age = input("what is your year of Birth?\n")
current_year = 2022
total = current_year - int(age)
print("Hello, " + name.upper() + ",\nYour age is " + str(total ))

# 5.PYTHON CODE FOR YES OR NO

print("Hello, Welcome to Python class!!!")
name = input("what is your name?\n")
if name == "ben":
    evil_status = input("Are you stranger??\n")
    if evil_status == "yes":
     print("You are not welocome here!!please get out")
     exit()
    else:evil_status == "no"
    print("You are most welocome here!!please get in!!\n")
    print("Hello " + name + " , thank you so much for learning.\n")
    menu = "python, java, c+,c++"
    print(name + ",What would you like from our courses today?\n\nHere is what we are teaching.\n\n" + menu)
else: 
    print("Hello " + name + " ,\nThank you so much for learning.\n")
    menu = "python, java, c+,c++"
    print(name + ",What would you like from our courses today?\n\nHere is what we are teaching.\n\n" + menu)
    order = input()

# 6.PYTHON CODE FOR TRUE OR FALSE

if 4 < 3:
    print("yep, it's true!!")
    print("It's still!!")
else:
    print("Nope, not true!!")



if 4 > 3:
    print("yep, it's true!!")
    print("It's still!!")
else:
    print("Nope, not true!!")

# 7.PYTHON CODE FOR SHOW SPECIFIC THINGS

supplies  = ["tent","water","foods","tea","coffee","mobile","dress"]
camp_site = ["crystal lake",404, 89.3, False]
#show specific things using print(supplies.pop(_))
supplies.extend(["fire","bed"])
print(supplies.pop(3))
supplies.pop(0)
print(supplies)

# 8.PYTHON CODE FOR REMOVING

supplies  = ["tent","water","foods","tea","coffee","mobile"]
camp_site = ["crystal lake",404, 89.3, False]
#Remove things using supplies.remove("____")
supplies.remove("tent")
print(supplies)

# 9.PYTHON CODE FOR REMOVE ANYWHERE

supplies  = ["tent","water","foods","tea","coffee","mobile","dress"]
camp_site = ["crystal lake",404, 89.3, False]
#Remove things using supplies.pop(_)
supplies.extend(["fire","bed"])
supplies.pop(0)
supplies.pop(2)
print(supplies)

# 10.PYTHON CODE FOR ORDER

print("Hello, Welcome to Python class!!!")
name = input("what is your name?\n")
print("hello " + name + " , thank you so much for learning.\n ")
menu = "python, java, c+,c++"
print(name + ",What would you like from our courses today? Here is what we are teaching.\n" + menu)
order = input()
price = 599
quantity = input("how many month you want python course?\n")
total = price * int(quantity)
print("Thank you so much for learning.\nHave a good day.\n Your total is: $" + str(total))
print("Sounds good "+ name + ", We'll have " + order + " class is ready for you in a moment")
print("Thank you...come back latter")
print("Done by $RAJESH$")

# 11.PYTHON CODE FOR CHOOSING

print("hello")
name = input("what is your name?\n")
print("Here what we are having,\npython!!\njava!!\nc+!!\nc++!!\nPlease enter what you want to")
menu = ("python, java, c++, c+. ")
order = input()
if order == "python":
    price = 13
    quantity = input("how many courese do you want\n ")
elif order == "java":
    price = 8
    quantity = input("how many courese do you want\n ")
elif order ==  "c++":
    price = 8
    quantity = input("how many courese do you want\n ")
elif order == "c+":
    price = 5
else:
    print("sorry, we don't have that here. ")
total = price * int(quantity)
print("Thank you so much for learning.\nHave a good day.\n Your total is: $" + str(total))

# 12.PYTHON CODE FOR CAMPING_LIST

camping_stuff = "tent,sleeping bags,water,foods"
print(camping_stuff)
#camping list starts from front 0,1,2,3,4,5,6,7,8,9,
#camping list starts from last -1,-2,-3,-4,-5,-6,-7,-8,-9,
camping_list = ["tent","water","foods","tea","coffee","mobile"]
camp_site = ["crystal lake",404, 89.3, True]
me = camping_list[4]
you = camping_list[5]
somebody = camping_list[-5]
print(me)
print(you)
print(somebody)


# 13.PYTHON CODE FOR ALLOWED

print("Hello, Welcome to Python class!!!")
name = input("what is your name?\n")
if name == "ben":
    print("You are not welocome here!!please get out")
else: 
    print("Hello " + name + " , thank you so much for learning.\n\n\n")
    menu = "python, java, c+,c++"
    print(name + ",What would you like from our courses today? Here is what we are teaching.\n" + menu)
    order = input()
    price = 599
    quantity = input("how many month you want python course?\n")
    total = price * int(quantity)
    print("Thank you so much for learning.\nHave a good day.\n Your total is: $" + str(total))
    print("Sounds good "+ name + ", We'll have " + order + " class is ready for you in a moment")
    print("Thank you...come back latter")
    print("Done by $RAJESH$")

# 14.PYTHON CODE FOR ADDING TWO ITEMS

supplies  = ["tent","water","foods","tea","coffee","mobile"]
camp_site = ["crystal lake",404, 89.3, False]
#Add missing things by using supplies.extend(["_____,_____"])
supplies.extend(["mask","sanitiser"])
print(supplies)

# 15.PYTHON CODE FOR SINGLE ITEM

supplies  = ["tent","water","foods","tea","coffee","mobile"]
camp_site = ["crystal lake",404, 89.3, False]
#Add missing thing by using supplies.append("______")
supplies.append("toilet paper.")
print(supplies)

# 16.PYTHON CODE FOR ADDING ANYWHERE

supplies  = ["tent","water","foods","tea","coffee","mobile"]
camp_site = ["crystal lake",404, 89.3, False]
#Add missing things anywhere using supplies.insert[0-?, "___"])
supplies.insert(0, "phone")
print(supplies)

# 17.PYTHON CODE FOR ADDING -VE ANYWHERE

supplies  = ["tent","water","foods","tea","coffee","mobile"]
camp_site = ["crystal lake",404, 89.3, False]
#Add missing things anywhere using supplies
supplies.insert(-3, "phone")

# 18.PYTHON CODE FOR GUESS GAME

print("Welcome to Guess Game")
secrets_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("guess the number:  "))
    guess_count  += 1
    if guess == secrets_number:
        print("Your guess is correct!!")
        break
    else:
     print("Sorry,Your guess is wrong(*-*)")
print(supplies)
