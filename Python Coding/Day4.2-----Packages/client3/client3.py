import sys

sys.path.append("C:\python selenium interview preparations\pythonHandsOn\Python Coding\Day4.2-----Packages\packA")
sys.path.append("C:\python selenium interview preparations\pythonHandsOn\Python Coding\Day4.2-----Packages\packB")
#
# import emp
# import stu
# obj = emp.Employee(1111111,"Shiva",111111)
# obj.disEmpDetails()
#
# obj2=stu.Student(11111111111111,"Muruga","AAAAAAA")
#
# obj2.disStuDetails()


from emp import *
from stu import *

obj = Employee(1111111,"Shiva",111111)
obj.disEmpDetails()

obj2=Student(11111111111111,"Muruga","AAAAAAA")
obj2.disStuDetails()
