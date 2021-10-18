weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in cms: "))
height = height/100
BMI = weight/(height*height)
print("Your Body Mass Index is : " ,BMI)
if(BMI>0):
    if(BMI<=18.5):
        print("You are Underweight")
    if(BMI>=18.5 and BMI<=24):
        print("You are Normal")
    if(BMI>=25 and BMI<=29.9):
        print("You are overweight")
    elif(BMI>30):
        print("You are Obese")
else:
    print("Invalid input")
