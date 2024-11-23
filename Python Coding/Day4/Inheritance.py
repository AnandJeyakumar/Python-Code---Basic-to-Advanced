# # # # #
# # # # # # example1
# # # # #
# # # # # class A:
# # # # #     def m1(self):
# # # # #         print("This is m1 from Class A")
# # # # # class B(A):
# # # # #     def m2(self):
# # # # #         print("This is m2 from Class B")
# # # # # obj=B()
# # # # # obj.m1()
# # # # # obj.m2()
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #with variables
# # # # #
# # # # class A:
# # # #     a,b=10,20
# # # #     def m1(self):
# # # #         print(self.a+self.b)
# # # # class B(A):
# # # #     x,y=10,20
# # # #     def m2(self):
# # # #         print(self.x*self.y)
# # # #
# # # # myob=B()
# # # # myob.m1()
# # # # myob.m2()
# # #
# # # #Multi level Inheritance Multiple parent and multiple child
# # #
# # # #
# # # # class Myclass1():
# # # #     a,b=10,20
# # # #     def m1(self):
# # # #         print(self.a+self.b)
# # # #
# # # # class Myclass2(Myclass1):
# # # #     x,y = 1000,500
# # # #     def m2(self):
# # # #         print(self.x/self.y)
# # # # class Myclass3(Myclass2):
# # # #     i,j=22,2
# # # #     def m3(self):
# # # #         print(self.i-self.j)
# # # #
# # # # myob =Myclass3()
# # # # myob.m1()
# # # # myob.m2()
# # # # myob.m3()
# # #
# # #
# # # # EX 4 heir
# # #
# # # # class Myclass1():
# # # #     a,b=10,20
# # # #     def m1(self):
# # # #         print(self.a+self.b)
# # # #
# # # # class Myclass2(Myclass1):
# # # #     x,y = 1000,500
# # # #     def m2(self):
# # # #         print(self.x/self.y)
# # # # class Myclass3(Myclass1):
# # # #     i,j=22,2
# # # #     def m3(self):
# # # #         print(self.i-self.j)
# # # #
# # # # myob =Myclass3()
# # # # myob.m1()
# # # # myob.m3()
# # #
# # #
# # # # Multiple Inheritance
# # #
# # # class A:
# # #     x,y=10,20
# # #
# # #     def m1(self):
# # #         print(self.x+self.y)
# # #
# # # class B:
# # #     a,z=100,11
# # #
# # #     def m2(self):
# # #         print(self.a + self.z)
# # #
# # # class C(A,B):
# # #     def m3(self):
# # #         print(self.x+self.z+self.y+self.a)
# # #
# # # obj = C()
# # # obj.m3()
# # # obj.m2()
# # # obj.m1()
# #
# # # Example 6 ---------Overriding
# # # using Super Function
# # # class Class1():
# # #
# # #     def m1(self):
# # #         print("Inside class 1")
# # #
# # # class Class2(Class1):
# # #     def m1 (self):
# # #         print("Inside class 2")
# # #         super().m1()
# # #
# # # myob=Class2()
# # # myob.m1() # --- the lateest one will get printed
# #
# #
# # # class Class1():
# # #
# # #     def m1(self):
# # #         print("Inside class 1")
# # #
# # # class Class2(Class1):
# # #     def m1 (self):
# # #         print("Inside class 2")
# # #
# # # myob=Class2()
# # # myob.m1() # --- the lateest one will get printed
# #
# #
# # # T0 Execute parent method in child then we go for super()
# # # class Class1():
# # #
# # #     def m1(self):
# # #         print("Inside class 1")
# # #
# # # class Class2(Class1):
# # #     def m1 (self):
# # #         print("Inside class 2")
# # #         super().m1()
# # #
# # # myob=Class2()
# # # myob.m1()
# #
# # #EX 7 Accessing parent variable from child\
# #
# #
# # class Parent:
# #     a,b=10,20
# #
# # class Child(Parent):
# #     x,y=1,2
# #     def m1(self,i,j):
# #         print(i,j)
# #         print(self.x,self.y)
# #         print(self.a,self.b)
# # myob = Child()
# # myob.m1(12,21)
#
# #
#
# #Overriding variabele - EX 8
# # class Parent:
# #     name = "Scott"
# #
# # class Child(Parent):
# #     name = "John"
# #     print(name)
# #
# # myob1 = Child()
# # myob2=Parent()
# # print(myob2.name)
#
#
# # overrding methods
#
# # class A:
# #     def m1(self):
# #         print("Hai")
# #
# # class B(A):
# #     def m1(self):
# #         print("B")
# #         super().m1()
# #
# # obj= B()
# # obj.m1()
#
# class Bank:
#     def rateOfInterest(self):
#         return 0
# class Bank1(Bank):
#     def rateOfInterest(self):
#         return 10
# class Bank2(Bank):
#     def rateOfInterest(self):
#         return 12
#
# myob1=Bank()
# interest1=myob1.rateOfInterest()
# print(interest1)
#
# myob2=Bank1()
# interest2=myob2.rateOfInterest()
# print(interest2)
#
# myob3=Bank2()
# interest3=myob3.rateOfInterest()
# print(interest3)


#Ex - 10 verloading Polymorplism
# Ex-1
# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print(name)
#         else:
#             print("No Value Provided")
#
# obj = Human()
# obj.sayhello("Allah")


# Ex 2 in Polymorphism

class cal():
    def sum(self,a=0,b=0,c=0):
        print(a+b+c)

mysum=cal()
mysum.sum(11)
mysum.sum(100,11)
mysum.sum(100,11,1000)

