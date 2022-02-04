# 1 .  Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string

def string_both_ends(input_string):
    if len(input_string) > 2:
        return input_string[:2] + input_string[-2:]
    elif len(input_string)==2:
        return input_string *2
    else:
        return -1

input_string = "w3resource"
print(string_both_ends(input_string))



# 2. .Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. 

def add_string(str):
    if len(str)>2:
        if str.endswith("ing"):
            str = str + "ly"
            return str
        else:
            str = str + "ing"
            return str
    else:
        return str

str = "string"
print(add_string(str))




# 3.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

s1,s2  = input("Enter the two strings seperated by space").split(" ")
print(s2[:2]+s1[2:]+" "+s1[:2]+s2[2:])
