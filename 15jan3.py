#WAP  to print symmetric  difference between two list


l1 = [4,5,6]
l2 = [6,7,8]


difference = set(l1).symmetric_difference(set(l2))
list_difference = list(difference)
print(list_difference)

