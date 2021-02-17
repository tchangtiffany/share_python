#add 2 numbers together

def add(num1, num2):
    result=num1+num2
    print(result)
add(5,3)
add(11.2,8.8)
add(10,-10)

#return values
def add(num1,num2):
    result=num1+num2
    return result
total=add(5,3)
print(total)

def subtract(num1,num2):
    result=num1-num2
    return result
total=subtract(5,3)
print(total)

def multiply(num1,num2):
    result=num1*num2
    return result
total=multiply(5,3)
print(total)

def greet(name, weather):
    message="Hi "+name+". It is a "+weather+" day"
    return message
greetings=greet("Sacha","rainy")
print(greetings)
greetings=greet("Carl","sunny")
print(greetings)

#simplifié encore de
def subtract(a,b):
    result =a-b 
    return result
operation=subtract(10,5)
print(operation)
#a :
def subtract(a,b):
    return a-b
    
print(subtract(10,5))