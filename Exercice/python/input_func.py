# print("Please enter your name:")
# name=input()
# print("Your name is "+name)


# x=input("Enter a number: ")
# y=input("Enter a second number: ")
# result=float(x)+float(y)
# message="The resul of "+x+" plus "+y+" is "+str(result)
# print(message)

# #converter with input (sans fonction)
# print("Enter a temperature in degrees Celsius: ")
# celsius=input()
# y = (float(celsius)*9/5)+32
# message= str(celsius) +" degrees Celsius are "+ str(y)+" degrees Farenheit."
# print(message)


#converter with input (avec fonction)
def temp_converter(celsius):
    msg_1=" degrees Celsius are "
    msg_2=" degrees Farenheit."
    result = (celsius*9/5)+32
    return str(celsius)+msg_1+str(result)+msg_2

user_input= input("Enter a temperature in degrees Celsius: ")
farenheit_result= temp_converter(float(user_input))
print(farenheit_result)