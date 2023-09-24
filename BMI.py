# BMI === Body Mass Index Calculator 
# Formula ===> Weight (kg) height (m^2)

weight = float(input("Enter your weight in KG: "))
height = float(input("Enter you height in Meter: "))

height_in_meter = (height * height)

BMI = float(weight/height_in_meter)

BMI_with_int= int(BMI)

print(BMI_with_int)