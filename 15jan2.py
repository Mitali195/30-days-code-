# WAP  to  print  all duplicates from a given list

li = [1,2,2,3,3,3,4,4,4,4]
d = Counter(li)

new_list = ([num for num in d[num]>1])
print(new_list)

