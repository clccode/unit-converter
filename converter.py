import math

def convert_km():
    km = num
    mi = round(km * 0.6214, 2)
    print(f"\n{km} kilometers is {mi} miles.")
    
def convert_mi():
    mi = num
    km = round(mi * 1.6, 2)
    print(f"\n{mi} miles is {km} kilometers.")
    
def convert_c():
    c = num
    f = math.ceil(c * 9/5 + 32)
    print(f"\n{c} degrees Celsius is {f} degrees Fahrenheit.")
    
def convert_f():
    f = num
    c = math.ceil((f-32) * 5/9)
    print(f"\n{f} degrees Fahrenheit is {c} degrees Celsius.")

def convert_ft():
    ft = num
    m = round(ft * 0.3048, 2)
    print(f"\n{ft} feet is {m} meters.")

def convert_m():
    m = num
    ft = round(m * 3.28084, 2)
    print(f"\n{m} meters is {ft} feet.")
    
def convert_kg():
    kg = num
    lbs = round(kg * 2.205, 3)
    print(f"\n{kg} kilograms is {lbs} pounds.")
    
def convert_lbs():
    lbs = num
    kg = round(lbs / 2.205, 3)
    print(f"\n{lbs} pounds is {kg} kilograms.")

print("## Welcome to the Unit Converter!##")
print("")
print("You can convert units of distance (km, mi), temperature (C, F), or weight (kg, lbs):")

convert = True 

while convert == True:
    unit = input("Please enter the unit you would like to convert: mi, km, C, F, ft, m, kg, or lbs: ").lower()
    num = float(input("Please enter the number you wish to convert: "))

    if unit == "km":
        convert_km()
    elif unit == "mi":
        convert_mi()
    elif unit == "c":
        convert_c()
    elif unit == "f":
        convert_f()
    elif unit == "ft":
        convert_ft()
    elif unit == "m":
        convert_m()
    elif unit == "kg":
        convert_kg()
    else:
        convert_lbs()   

    go_again = input("\nWould you like to go again? Enter 'y' or 'n': ").lower()
    
    if go_again == "y":
        convert = True
    else:
        convert = False
        print("\nThanks! Have a nice day.")
