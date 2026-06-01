def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi, category = calculate_bmi(weight, height)

print("BMI:", round(bmi, 2))
print("Category:", category)
