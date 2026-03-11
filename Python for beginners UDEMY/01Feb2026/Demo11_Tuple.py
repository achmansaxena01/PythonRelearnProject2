#   Tuple is like list, but it cannot be modified ( immutable)
#   we use it where we need a read only list, and it need not be modified
#   it maintain the insertion order
#   it can have heterogeneous elements (different types of data)
#   it can be defined as  t=(1,2,3,4) but bracket is optional
#   brackets are optional, but they are recommended to enhance readability
#   single element is followed by , else it will be treated as general variable.
T1 = (11, 12, 13, 'retro', 14, 14, 14)
T2 = 21, 22, 23, 24, 25, 25
T3 = 5,

print(T1)
print(T1 * 3)
print(T1.count(14))
print(T1.index(14))
print(T1[:5])  # to trim the tuple
