
# # The name and age
# question
# def greet(name, age):
#     message = "Your name is" + name + " and you are " + int(age) + " years old."
#     return message

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(greet(name, age))

# #Réponse
# def greet(name, age):
#     message = "Your name is " + name + " and you are " + age + " years old."
#     return message

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(greet(name, age))


# # # #The calculator
# # question 
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# num_one = input("Enter a number: ")
# num_two = input("Enter another number: ")

# message = "The result of " + num_one + " + " num_two + " is " + add(num_one, num_two)
# print(message)

# message = "The result of " + num_two + " - " + num_one + " is " + subtract(num_one, num_two)
# print(message)

# réponse

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# num_one = input("Enter a number: ")
# num_two = input("Enter another number: ")

# message = "The result of " + num_one + " + " + num_two + " is " + str(add(int(num_one), int(num_two)))
# print(message)

# message = "The result of " + num_one + " - " + num_two + " is " + str(subtract(int(num_one), int(num_two)))
# print(message)


#DO you like programming

#question

# def get_result(answer):
#     if answer == a:
#         return true
#     else
#         return false

# print("Do you like programing?")
# print("a. Yes")
# print("b. No")
# result = input("Enter a or b: ")

# if get_result(result):
#     print("Awesome! Programming is really fun!")
# else
# print("Hang in there! It's an acquired taste!")

#réponse
def get_result(answer):
    if answer == "a":
        return True
    else:
        return False

print("Do you like programing?")
print("a. Yes")
print("b. No")
result = input("Enter a or b: ")

if get_result(result):
    print("Awesome! Programming is really fun!")
else:
    print("Hang in there! It's an acquired taste!")