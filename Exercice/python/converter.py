#conversion celsius Farhenheit
# celsius = 21
# Farhenheit = (celsius*9/5)+32
# print(Farhenheit)

# celsius = -5
# Farhenheit = (celsius*9/5)+32
# print(Farhenheit)

# celsius = 17
# Farhenheit = (celsius*9/5)+32
# print(Farhenheit)

# def convert(celsius):
#     return (celsius*9/5)+32
    
# print(convert(21.5)) 
# print(convert(-7)) 
# print(convert(11)) 
# print(convert(0)) 

# def convert(celsius):
#      farenheit = (celsius*9/5)+32
#      message = str(celsius) +" degrees Celsius are " + str(farenheit)+" degrees Farenheit."
#      return message

# print(convert (21.5))
# print(convert (-7))
# print(convert (11))
# print(convert (0))

# Converter with conditional logic
def temp_converter(celsius):
    msg_1=" degrees Celsius are "
    msg_2=" degrees Farenheit."
    result = (celsius*9/5)+32
    return str(celsius)+msg_1+str(result)+msg_2

user_input= input("Enter a temperature in degrees Celsius: ")
farenheit_result= temp_converter(float(user_input))

if float(user_input) >38 :
     print("It's really hot!")

print(farenheit_result)

