# # # # # # # # # name="anand"
# # # # # # # # # name2='anand'
# # # # # # # # # name3=str('O')
# # # # # # # # # name4=str("adsdas")
# # # # # # # # #
# # # # # # # # # # Creating Empty Strings
# # # # # # # # #
# # # # # # # # # s=""
# # # # # # # # # t=''
# # # # # # # # # b=str()
# # # # # # # # #
# # # # # # # # # # >Mutable - can be changed
# # # # # # # # # # Immutable = cannot be changed
# # # # # # # # #
# # # # # # # # # # String is Immutable
# # # # # # # # #
# # # # # # # # # str1='welcome'
# # # # # # # # # print(id(str1))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # str1=str1+'pytin'
# # # # # # # # # print(str1)
# # # # # # # # # print(id(str1))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # # If the values change it is called Immutable
# # # # # # # #
# # # # # # # #
# # # # # # # # # Example 2
# # # # # # # #
# # # # # # # # # + and * for String
# # # # # # # # #
# # # # # # # # # str="Hai"
# # # # # # # # # print(str+"Gaia")
# # # # # # # # #
# # # # # # # # # print(str*3)
# # # # # # # #
# # # # # # # # # Slicing Concept
# # # # # # # #
# # # # # # # # # starting index is 0
# # # # # # # # # ending index count from 1 (n-1)
# # # # # # # # str= "Welcome"
# # # # # # # #
# # # # # # # #
# # # # # # # # print(str[1:3])
# # # # # # # #
# # # # # # # # print(str[:6])
# # # # # # # # print(str[2:])
# # # # # # # #
# # # # # # # # print(str[0:-1])
# # # # # # # # print(str[0:-2])
# # # # # # # #
# # # # # # # # Example 5
# # # # # # #
# # # # # # # # ord() and chr() ----ascii number
# # # # # # #
# # # # # # #
# # # # # # # print(ord('A'))
# # # # # # # print(chr(65))
# # # # # # #
# # # # # # #
# # # # # # # Example 6
# # # # # # #
# # # # # # print(max('abc'))
# # # # # # print(min('abc'))
# # # # # #
# # # # # # print(len("adsfsf"))
# # # # # #
# # # # #
# # # # #
# # # # # # example 7
# # # # #
# # # # # # In or not in operators with strings
# # # # # # it will retrun boolean value
# # # # #
# # # # # strq = "Welcome"
# # # # #
# # # # # print("me" in strq)
# # # # #
# # # # # print('e' not in strq)
# # # #
# # # #
# # # # # string comparison
# # # #
# # # # a="a"
# # # # b = "a"
# # # # print(a==b)
# # #
# # #
# # # # Testing strings
# # #
# # # sui = "Welcome to PYTHON"
# # #
# # # print(sui.isalnum())
# # # print("Welcomw".isalpha())
# # # fg="23".isnumeric()
# # # print(fg)
# # #
# # # print(sui.lower())
# #
# #
# # # example 10
# #
# # # substrings
# #
# # hui="welcomeopopopo"
# # print(hui.count('o'))
# #
# #
# #
# #example 11
#
# # captitalize
#
# s = "anand sest tsdf"
# print(s.capitalize())
#
#
# print(s.lower())
#
# print(s.title())
# print(s.upper())
#
# print(s.replace("sest","Shiva"))
#
#
#
#
# # Important one
#
# # How to reverse a string
#Method 1
# i will get last character
s = "welcome"
rev=''
for i in s:
    rev=i+rev
print(rev)

# Method 2

aa="Shiv"
rev_str=str(aa[::-1])

print(rev_str)
print(type(rev_str))