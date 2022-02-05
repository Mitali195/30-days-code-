# 1. Write a python program to filter a list of integers using lamda

l = [1,2,3,4,5,6,7,8,9,10]
print('Original list of integers is\n',l)

even_nums = list(filter(lambda x:x%2 == 0,l))
print('Even numbers from the said list is:\n',even_nums)

odd_nums = list(filter(lambda x:x%2 == 1,l))
print('Odd numbers from the said list is:\n',odd_nums)



# 2. Write a python program to add two given list using map and lamda:

l1 =[1,2,3]
l2 =[4,5,6]
print(f"Original list is:\n{l1}\n{l2}")

Result = map(lambda x,y : x+y,l1,l2)
print("Result: After adding two list:")
print(list(Result))



# 3. Write a program that prints all the numbers from 0 to 6 expect 3 and 6:

for x in range(0,6):
  if (x == 3 or x == 6):
    continue
  print(x)  
  


