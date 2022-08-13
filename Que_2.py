# Write a Python program to reverse a string.
def reverse(s): 

  str = " " 

  for string in s: 

    str = string + str

  return str

s = input("Enter the string : ")

print ("The original string  is : ",end="") 

print (s) 

print (" After reverse the string vis : ",end="") 

print (reverse(s))