
#Appoach 1 -- if we give like this it os nthrow execpetion error in line 8 and the next lines will not be executed
#
# print("First Line")
# print("Second Line")
# print("Third Line")
# print("Fourth Line")
# print(x)
# print("Sixth Line")
# print("seventh Line")
# print("Program completed")
# The Right appoach is
# print("First Line")
# print("Second Line")
# print("Third Line")
# print("Fourth Line")
# try:
#     print(x)
# except:
#     print("Execption has ocurred and handled")
# print("Fifth Line")
# print("Six Line")
# print("Program completed")


# Apprach 2 By Provinging the Exception name and handling it
# #
# print("First Line")
# print("Second Line")
# print("Third Line")
# print("Fourth Line")
# try:
#     num =10/0
#     # print(x)
# except ZeroDivisionError:
#     print("ZeroDivisionError has occurred and handled")
# print("Fifth Line")
# print("Six Line")
# print("Program completed")


#Approch Multiple Excepts block
#
# try:
#     num1,num2=10,5
#     result = num1/num2
# except ZeroDivisionError:
#     print("The ZeroDivisionError error has occurred and handled ")
# except SyntaxError:
#     print("The SyntaxError error has occurred and handled ")
# except:
#     print("Execption has ocurred and handled")
# else:
#     print("No Exception error has occured")
# finally:
#     print("Final Line")
#     print("Program Completed............")
#



#Apprach raising a new exception-------


def enterNum(num):
    if num<0:
        raise ValueError("The Given num is not int")
    if num %2 == 0:
        print("The Num is Even")
    else:
        print("The Num is ODD")


try:
    enterNum(-1)
except ValueError :
    print("ValueError Exception handled")

print("Completed.......")



























































































