print("Please type in your weight in kg:")
weight = input()
print("Please type in your height in cm:")
height = input()

weight_in_int = int(weight)
height_in_int = int(height)

bmi = weight_in_int / ((height_in_int/100) ** 2)
answer = "Your BMI is " + str(bmi) + ", "
if bmi<=17.5:
    answer+="you are underweight."
elif 17.5<bmi<=24:
    answer+="you have a normal weight."
elif 24<bmi<=29:
    answer+="you are overweight."
elif 29<bmi<=34:
    answer+="you are very overweight."
elif 34<bmi:
    answer+="you have obesity."

print(answer)