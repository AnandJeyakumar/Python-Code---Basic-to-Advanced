# #
# #
# # # Range of Indexes
# #
# # mylist1=["apple","Banana","Cherry","Donald","Elephant","Fish","Giraffe"]
# #
# # # starting index : end index --the end value will be n-1
# #
# # print(mylist1[2:6])
#
# # Change Item in List
# # mylist=["apple","Banana","Cherry","Donald","Elephant","Fish","Giraffe"]
# # print(mylist)
# # mylist[2]=10000
# # print(mylist)
# #
# # # Print in Order Wide
# # # mylist=["apple","Banana","Cherry","Donald","Elephant","Fish","Giraffe"]
# #
# # for i in mylist:
# #     print(i)
#
# #Checking the item is present or not
# # mylist=["apple","Banana","Cherry","Donald","Elephant","Fish","Giraffe"]
# #
# # for i in mylist:
# #     if 'd'==i:
# #         print("The Item is present")
# #         break
# #     else:
# #         print("Not present")
#
#
#
# # Finding Length
# # mylist=["apple","Banana","Cherry","Donald","Elephant","Fish","Giraffe"]
# # print(len(mylist))
#
#
# # Add items into list - ----- append , insert
# # # Insert (Index,"ItemValue")
#
# # mylist1=["apple","Banana","Cherry"]
# # mylist1.append("Shiva")
# # print(mylist1)
# #
# #
# # mylist=["apple","Banana","Cherry"]
# # mylist.insert(1,"Big")
# # print(mylist)
#
#
# # Remove items from the list -----pop   , del , clear
#
#
# #pop  ----index
# # mylist=["apple","Banana","Cherry"]
# # mylist.pop(0)
# # print(mylist)
#
# #Del   ------index   ---it is a keyword
# # mylist=["apple","Banana","Cherry"]
# # del mylist[2]
# # print(mylist)
#
#
# #Clear -------- it will clear all the item in the list
# # mylist=["apple","Banana","Cherry"]
# # mylist.clear()
# # print(mylist)
#
# # # To Copy the data from one list to another
# mylist1=["apple","Banana","Cherry"]
# mylist2=list(mylist1)
# print(mylist2)
#
#
# a=["apple","Banana","Cherry"]
# b=a.copy()
# print(b)


# Combining
# mylist1=["apple","Banana","Cherry"]
# mylist2=["Donald","Elephant","Fish"]
#
# my3=mylist1+mylist2
# print(my3)
# my3=mylist2+mylist1
# print(my3)


# Merging data by using append
# mylist1=["apple","Banana","Cherry"]
# mylist2=["Donald","Elephant","Fish"]
# for i in mylist2:
#     mylist1.append(i)
#
# print(mylist1)

#Extend extend()
# mylist1=["apple","Banana","Cherry"]
# mylist2=["Donald","Elephant","Fish"]
# print(id(mylist2))
# mylist2.extend(mylist1)
# print(mylist2)
# print(id(mylist2))