# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("BMI caluclator")

#taking input for cal. BMI

height = float(input("enter the height (in m) = "))
weight = float(input("enter the weight = "))

#BMI logic

BMI = weight/height**2

#printing thr BMI
print( BMI )

#if else cond.
if BMI <= 18.5:  
    print("You are underweight")  
elif BMI <= 24.9:  
    print("You are healthy.")  
elif BMI <= 29.9:  
    print("You are over weight.")  
else:  
    print("You are obese.")  
