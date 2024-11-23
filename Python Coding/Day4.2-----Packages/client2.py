# Approach 1

# import sys
# sys.path.append("C:\python selenium interview preparations\pythonHandsOn\Python Coding\Day4.2-----Packages\package1")
#
# sys.path.append("C:\python selenium interview preparations\pythonHandsOn\Python Coding\Day4.2-----Packages\package1\package2")
#
# import module1
# module1.display()
#
# import module2
# module2.show()


# Approach 2

import sys
sys.path.append("C:\python selenium interview preparations\pythonHandsOn\Python Coding\Day4.2-----Packages\package1")

sys.path.append("C:\python selenium interview preparations\pythonHandsOn\Python Coding\Day4.2-----Packages\package1\package2")


from module1 import *
from module2 import *

display()
show()