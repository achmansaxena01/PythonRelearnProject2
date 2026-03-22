p_marks = int(input("enter the marks of student in physics out of 100 : "))
c_marks = int(input("enter the marks of student in chemistry out of 100 : "))
m_marks = int(input("enter the marks of student in maths out of 100 : "))

if p_marks > 35 and c_marks > 35 and m_marks > 35:
    print("student has passed the exam : ")
    grade = (p_marks + c_marks + m_marks)/3
    print(f"grade of the student : {grade}")
    if grade <= 59 :
        print("grade of the student is C ")
    elif grade <= 69 :
        print("grade of the student is B ")
    else:
        print("grade of the student is A ")
else:
    print("student has failed the exam : ")