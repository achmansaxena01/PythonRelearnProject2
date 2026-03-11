students = {"john": ["python", "Django", "Drf"]
    , "bob": ["Java", "SpringBoot"]
    , "Jim": ["js", "Node", "react "]}

keys = students.keys()
print(keys)

for i in keys:
    print("Courses take by each ", i, "are")
    for j in students[i]:
        print(j)
    print("----------------")

print("this is end*****************************")