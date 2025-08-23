lst1 = []
print(lst1)

lst2 = [10, 20, 30, 'abc', 10]
print(lst2)
# we can do indexing , slicing and other functions on this too.

print(lst2[3])
print(lst2[2:5])
print(lst2 * 3)
lst1.append(56.78)  # to append the list
print(lst1)
lst2.remove(10)  # remove by value
print(lst2)
del (lst2[2])
print(lst2)

#   lst1.clear()    # to clear the data in the list
#   print(lst1)


print(max(lst2))
print(min(lst2))
lst2.insert(5, 234)
print(lst2)

lst2.sort()
print(lst2)

lst2.sort(reverse=True)
print(lst2)
