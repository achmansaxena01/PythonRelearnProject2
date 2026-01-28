student_info = {'name': 'Achman', 'age': 32, 'major': 'Engineering'}

print(student_info)
print(student_info['name'])
print(student_info['age'])

student_info['email'] = 'anubhav.23@gmail.com'
print(student_info['email'])

student_info['age'] = 22
print(student_info['age'])
print(student_info)

del student_info['major']
print(student_info)

