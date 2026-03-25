# 1. ask user for age, weight, gender, creatine concentration
# 2. check if inputs are valid:
#    age < 100, weight > 20 and < 80, Cr > 0 and < 100, gender is male or female
# 3. if not valid, print error and stop
# 4. calculate CrCl = ((140 - age) * weight) / (72 * Cr)
# 5. if female, multiply by 0.85
# 6. print the result

age = int(input("Please enter the patient's age in years: "))
weight = float(input("Please enter the patient's weight in kg: "))
gender = input("Please enter the patient's gender ('male' or 'female'): ")
cr = float(input("Please enter the patient's creatine concentration in µmol/l: "))

# validate inputs first
if age >= 100:
    print("Error: Age needs to be corrected (must be < 100 years).")

elif weight <= 20 or weight >= 80:
    print("Error: Weight needs to be corrected (must be > 20 and < 80 kg).")

elif cr <= 0 or cr >= 100:
    print("Error: Creatine concentration needs to be corrected (must be > 0 and < 100 µmol/l).")

elif gender != "male" and gender != "female":
    print("Error: Gender needs to be corrected (must be 'male' or 'female').")

else:
    # Cockcroft-Gault equation
    crcl = ((140 - age) * weight) / (72 * cr)
    
    if gender == "female":
        final_crcl = round(crcl * 0.85, 2)  # multiply by 0.85 for female
    else:
        final_crcl = round(crcl, 2)
        
    print("The calculated CrCl is: " + str(final_crcl))
