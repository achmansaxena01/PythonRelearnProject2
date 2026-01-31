Height = 6.2
Weight = 85

# BMI = weight in KG/(Height in metre)^2
HeightInMetres = Height*0.4536

Bmi = Weight/(HeightInMetres * HeightInMetres)
print("Bmi of the person is " , Bmi)
