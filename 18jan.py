# 1. Write a Python program to calc. the length of the string without using built-in func

str= 'Mitali'
len = 0
while str[len:]:len+=1
print('str',len)


# 2. Write a python function to revesre a string if its length is a multiplt of 4 without using in function:
name = "Mitali"
number = 'four'
print(name[::-1])
print(number[::-1])

#3. Write a python program to print the index of the character in a string
str =  'w3resources'
for index, char  in enumerate(str):
    print(f'Current character is {char} position at {index}')

