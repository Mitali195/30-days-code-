# 1. WAP IN PYTHON TO CREATE A  DICTIONARY FROM A STRING


str1 = 'w3resources'
my_dic = {}
for i in str1:
  my_dic[i] = my_dic.get(i,0) + 1
  print(my_dic)
  
  
  
  
# 2. WAP  IN PYTHON TO SORT A LIST IN ALPHABETICALLY IIN A DICTONARY

a = {'n1':[2,3,1],'n2':[5,1,2],'n3':[3,2,4]}
sorted_li = {x:sorted(y) for x,y in a.items()}
print(sorted_li)





# 3 . WAP IN PYTHON  TO COMBINE 2 LIST INTO DICTONARY
x = ['a','b','c','d','e','f']
y = [1,2,3,4,5]

print(dict(zip(x,y)))
