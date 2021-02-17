# #The conversion from ml to m3
# # 1m3=1000L=1000000ml=10^6ml
# def convert(ml):
#     m3=ml/1e6
#     message="The conversion from "+str(ml)+" ml is "+ str(m3)+" m3."
#     return message
# print(convert(1000000))

#The conversion from ml to m3 with conditional logic
# 1m3=1000L=1000000ml=10^6ml

def convert(ml):
    m3=ml/1e6
    message="The conversion from "+str(ml)+" ml is "+ str(m3)+" m3."
    return message

user_input= input("Enter the ml you want to convert to m3 ")

print(convert(float(user_input)))

if float(user_input) >= 1.2e6:
    print("It's more than from my well")