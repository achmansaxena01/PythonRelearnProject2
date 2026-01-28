lst1 = [10, 20, 30,'', 40 ]
print(lst1)

tpl1 = tuple(lst1)
print(tpl1)
print(type(tpl1))
'''
List can not be used as key in the dictionary but a tuple can because 
to be the key the the object should be hashable and mutable which is not the case with list
'''

