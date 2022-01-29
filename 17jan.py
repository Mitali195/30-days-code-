# 1. UPDATE  THE  FIRST SET WITH ITEMS THAT DON'T EXIST IN THE.
#GIVEN:  SET1 ={10,20,30}    SET2= = {20,40,50}
#EXPECTED OUTPUT : SET1{10,30}

set1 = {10,20,30}
set2 = {20,40,50}
print("Set1:",set1.difference(set2))



# 2. RETURN A SET OF ELEMENTS PRESENT IN SET A OR B, BUT NOT BOTH)

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print(set1.symmetric_difference(set2))



# 3. REMOVE ITEMS FROM  BOTH SET1 THAT ARE NOT COMMON TO BOTH SET1 AND SET2:

set1 ={10,20,30,40,50}
set2 ={30,40,50,60,70}
print(set1.intersection(set2))
