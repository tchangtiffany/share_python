# day=True 
# night=False
# print(day)
# print(night)

# print(5==5) # true
# print (2==5) #false
# print (5!=5) # it return false

# secret_number=5
# guess= input("Enter a number between 1 and 10: ")
# print(secret_number==int(guess))

# secret_word = "kiwi"
# guess = input("Enter the secret word : ")
# print(secret_word==str(guess))

## if this, then that !

# password="secret"
# user_input=input("Enter the password: ")
# if password==user_input:
#     print("You are now logged in.")

# weather="rainy"
# if weather =="sunny":
#     print("It's sunny outside")
#     print("It's great")
# print("This line of code will execute no matter what")


# # greater and smaller
# appes=3
# oranges=3
# if apples>=oranges:
#     print("There are less apples than oranges...")
#     print("... or the same amount")

#Exercise:find the result

# user_input=input("What is the result of 5+2 ?")
# if user_input== "7":
#     print("Correct!")
# if user_input!= "7":
#     print("Try again")

# result=7
# user_input=input("What is the result of 5+2 ?")
# if user_input== int(result):
#     print("Correct!")
# if user_input!= int(result):
#     print("Try again")

# secret_word = "kiwi"
# guess = input("Enter the secret word : ")
# if secret_word==guess:
#     print("Bravo")
# else:
#     print("Oops it's not the secret word")

# print("Let's play again!")


# weather="sunny"

# if weather =="rainy":
#     print("Take an umbrella")
# elif weather =="sunny":
#     print("Take sunglasses")
# elif weather =="snowing":
#     print("Take gloves")
# else:
#     print("Stay at home")



# input1=input("Enter a first number: ")
# input2=input("Enter a second number: ")
# result= float(input2)-float(input1)

# if result>10:
#     print("The result is greater than 10")
# elif result>0:
#     print("The result is greater than 0 but not than 10")
# elif result ==0:
#     print("The result is 0")
# else:
#     print("The result is a negative number")
# print("You can try again!")



#AND AND AND
# weather="sunny"
# temperature="cold"
# if weather=="sunny" and temperature=="warm":
#     print("Take sunglasses and a tshirt")


# input1=input("Enter a first number: ")
# input2=input("Enter a second number: ")
# if float(input1)>10 and float(input2)>10:
#     print("Both numbers are greater than 10")
# else:
#     print("At least one of the numbers you entered is not greater than 10")

# # Ex 2 AND

# weather="raining"
# temperature="cold"
# msg1="If it's "
# msg2=" and if it's "
# if weather=="raining" and temperature=="cold":
#     print(msg1+weather+msg2+temperature+" take an umbrella and a warm jacket.")
# elif weather=="raining" and temperature=="warm":
#     print(msg1+weather+msg2+temperature+" take an umbrella and a tshirt.")
# elif weather=="sunny" and temperature=="cold":
#     print(msg1+weather+msg2+temperature+" take sunglasses and a warm jacket.")
# elif weather=="sunny" and temperature=="warm":
#     print(msg1+weather+msg2+temperature+" take sunglasses and a tshirt.")
# else:
#     print("If it's anything else, stay home")

# OR OR
# a = 8
# b = 12
# if a > 10 or b > 10:
#     print("At least one of the two numbers is greater than 10!")
# else:
#     print("Both numbers are not greater than 10.")

# # Ex and + or
#     # If the language is Python or JavaScript, it is a good course.
#     # If the languages are Python and JavaScript, this is the Thinking and Creating with Code course.
#     # If the number is bigger than 10 or the color is blue, the test is true.
#     # If the number is not bigger than 10 and the color is not blue, the test is true.

# lang="Python"
# lang2="JS"
# numb=12
# color="red"

# if lang=="Python" or lang2=="JS":
#     print("If the language is Python or JavaScript, it is a good course.")
# elif lang=="Python" and lang2=="JS":
#     print("If the languages are Python and JavaScript, this is the Thinking and Creating with Code course.")

# if numb>10 or color=="blue":
#     print("If the number is bigger than 10 or the color is blue, the test is true.")
# elif numb<10 and color!="blue":
#     print("If the number is not bigger than 10 and the color is not blue, the test is true.")

# # GAME : guess the number and the color

# input_num=input("Type a number between 1 and 20: ")
# input_color=input("Type a color: ")
# secret_num=14
# secret_color="grey"

# if input_num==secret_num and input_color==secret_color:
#     print("You've found both the secret number and the secret color!")
# elif input_num==secret_num or input_color==secret_color:
#     print("You found at least one of the secrets!")
# else:
#     print("You didn't find any of the secrets!")
#     print("Better luck next time!")

# print("Try again")

# idem mais within a function

secret_num=14
secret_color="grey"

def guess():
    input_num=input("Type a number between 1 and 20: ")
    input_color=input("Type a color: ")
    if int(input_num)== secret_num and input_color==secret_color:
        print("You've found both the secret number and the secret color!")
    elif int(input_num)==secret_num or input_color==secret_color:
        print("You found at least one of the secrets!")
    else:
        print("You didn't find any of the secrets!")
        print("Better luck next time!")

guess()
print("Try again")