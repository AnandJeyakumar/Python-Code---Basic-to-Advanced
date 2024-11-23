# # # #
# # # #
# # # # class myclass():
# # # #     def fun(self):
# # # #         pass
# # # #     def fun2(self,name):
# # # #         print("Hai ",name)
# # # #
# # # # myobj = myclass()
# # # # myobj.fun()
# # # # myobj.fun2("SHIVA")
# # # #
# # # # boj1=myclass()
# # # # boj1.fun2("Vel")
# # #
# # #
# # # # Example2
# # #
# # # # instance method need to create an object
# # # # Statis method we can directly use
# # #
# # # class myclass():
# # #     def m1(self):
# # #         print("Hai")
# # #
# # #     @staticmethod
# # #     def m2(number):
# # #         print(number)
# # #
# # # myclass.m2(1111)
# # # cl=myclass()
# # # cl.m1()
# # #
# #
# #
# # # Types of Variables
# #
# # # Global , Class , Local   - variables
# #
# #
# # class myclass:
# #
# #     a,b=111,1000
# #
# #     def add(self):
# #         print(self.a+self.b)
# #
# #     def mul(self):
# #         print(self.a*self.b)
# #
# # obj=myclass()
# # obj.add()
# # obj.mul()
#
#
# # global , class , local
#
# a,b = 10,20       #Global Variable
#
# class myClass():
#     c,d = 15,25   # Class Variable
#
#     def fun(self,e,f):   # e,f is a local variable
#         print(e,f)     # Printing the value of e,f
#         print(self.c+self.d)    # Printing class variable
#         print("The global without method",a*b)
#         print("The global",globals()['a'])
#         print(globals()["a"]*globals()["b"])   # Print global variables - globals()["Variablename"]
#
# myo=myClass()
# myo.fun(30 , 50 )


# ===================================
# constructor  - name is fixed ===== __init__(self)
# It will not return any value
# It can take arguments and parameter
# no need to create any object , it will automatically invoke when object creation



class demo:

    def __init__(self,name):
        print("This is Constructor triggered by", name)

    def normal(self,name):
        print(name)

obj=demo(11111)
obj.normal("Hai")

