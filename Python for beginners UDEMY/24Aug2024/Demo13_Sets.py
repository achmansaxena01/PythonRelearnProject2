# sets does not allow duplicates
# it does not guarantee any order
s1 = {10, 20, 30, "xyz", 40, 25, 40}
print(s1)
print(type(s1))
print(len(s1))

s1.update([33, 35])
print(s1)
print(len(s1))
# we can not do indexing ,slicing , repetition
s1.remove(40)
print(s1)

f1 = frozenset(s1)  # frozenset does not allow adding and removing the elements
# f1.update([21])
# f1.remove(20)
print(f1)
print(type(s1))
print(len(s1))
