#user input of Data


name= input("Name: ")
age= input("Age: ")
"""why i can use float same line .
 code ok but not execute 
like 
age= input(float(Age))"""
Gender=input("Gender: ")
Weight=input("weight in Kg: ")
Weight=float(Weight)
# hight= input("input hight in feet and inches:)
"""
hight=(float("enter hight")) 
line 13, in <module>
    hight=(float("enter hight"))
ValueError: could not convert string to float: 'enter hight'"""
hight=input("enter hight:  ")
hight=float(hight)
hight=hight*0.3048
bmi =Weight /(hight**2)
print("Check details  "+  name, age, Gender, Weight,)
print("Is it ok your information?")
conformation= input("""
Please Type Ok
 if your information is correct! 
Otherwise try again!
Type Ok: """)
# Calculate ideal weight range for normal BMI (18.5 to 24.9)
min_weight = 18.5 * (hight ** 2)
max_weight = 24.9 * (hight ** 2)


# Determine BMI category
if bmi < 18.5:
    category = "Underweight . Please gain weight by consulting a doctor ! "
# Weight to gain to reach minimum normal weight
elif 18.5 <= bmi < 24.9:
    category = "Normal weight. Your health condition is good . Stay healthy! "
elif 25 <= bmi < 29.9:
    category = "Overweight. Please reduce weight by consulting a doctor !"
else:
    category = """Obesity ! Please reduce weight
     by consulting a doctor and
      take daily excercise  !"""
print("Your body mass index is:")
print(bmi)
print(category)
print("Thank you for using our software!" )

