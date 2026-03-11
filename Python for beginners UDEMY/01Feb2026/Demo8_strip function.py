s = "  You are awesome "
print(s)

s1 = """ you are 
the creator
of your destiny """
print(s1)

print(s[2])  # Gives value at that index
print(s * 2)  # Populate the string twice
print(s * 3)  # Populate the string thrice
print(len(s))  # return the length of the string
print(s[0:6])  # to trim the string but does not include the value at the last mentioned index
print(s[0:])
print(s[:8])
print(s[-3:-1])  # to trim the string but does not include the value at the last mentioned index
print(s[0:9:2])
print(s[15::-1])
print(s.strip())  # to remove leading and trailing bank spaces
print(s.lstrip())  # to remove leading bank spaces
print(s.rstrip())  # to remove trailing bank spaces
print(s.find("awe", 0, len(s)))  # to fins a substring in the given string
print(s.count("a"))  # to counts occurrence of a
print(s.replace("awesome", "super"))  # to replace a part of string

print(s.upper())
print(s.lower())
print(s.title())
