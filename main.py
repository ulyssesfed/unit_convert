# Define a dictionary of conversion factors for distance units
distance_conversions = {
    "millimeters": 1000,
    "centimeters": 100,
    "meters": 1,
    "kilometers": 0.001,
    "inches": 39.3701,
    "feet": 3.28084,
    "yards": 1.09361,
    "miles": 0.000621371,
    "nautical miles": 0.000539957,
    "parsec": 3.24078e-17,
    "astronomical units": 6.68459e-12,
    "furlongs": 0.00497097,
    "fathoms": 0.546807,
    "cubits": 0.546807,
    "rods": 0.198838,
    "chains": 0.0497094,
    "leagues": 0.000207123,
    "angstroms": 1e+10,
    "microns": 1e+6,
    "nanometers": 1e+9,
    "picometers": 1e+12,
    "femtometers": 1e+15,
    "attometers": 1e+18,
    "light seconds": 3.33564e-9,
    "light minutes": 5.559e-11,
    "light hours": 9.265e-13,
    "light days": 3.839e-14,
    "light weeks": 5.479e-15,
    "light months": 1.368e-15,
    "light years": 1.057e-16,
    "light decades": 1.057e-17,
    "light centuries": 1.057e-18,
    "light millennia": 1.057e-19,



}

# Define a dictionary of conversion factors for temperature units
temperature_conversions = {
    "celsius": 1,
    "fahrenheit": 9/5,
    "kelvin": -273.15,
    "rankine": 9/5,
    "reaumur": 4/5,
    "romer": 21/40,
    "newton": 33/100,
    "delisle": -100/3
}

weight_conversions = {
    "milligrams": 1000000,
    "grams": 1000,
    "kilograms": 1,
    "metric tons": 0.001,
    "ounces": 35.274,
    "pounds": 2.20462,
    "stones": 0.157473,
    "short tons": 0.00110231,
    "long tons": 0.000984207
}
time_conversions = {
    "nanoseconds": 1000000000,
    "microseconds": 1000000,
    "milliseconds": 1000,
    "seconds": 1,
    "minutes": 0.0166667,
    "hours": 0.000277778,
    "days": 0.0000115741,
    "weeks": 0.0000016534,
    "months": 0.000000380517,
    "years": 0.0000000317098,
    "decades": 0.00000000317098,
    "centuries": 0.000000000317098,
    "millennia": 0.0000000000317098
}
volume_conversions = {
    "milliliters": 1000,
    "liters": 1,
    "cubic meters": 0.001,
    "cubic kilometers": 1e-9,
    "cubic inches": 61.0237,
    "cubic feet": 0.0353147,
    "cubic yards": 0.00130795,
    "cubic miles": 2.399e-10,
    "cubic decimeters": 1000,
    "cubic centimeters": 1000000,
    "cubic millimeters": 1000000000,
    "imperial gallons": 0.219969,
    "imperial quarts": 0.879877,
    "imperial pints": 1.75975,
    "imperial cups": 3.51951,
    "imperial fluid ounces": 35.1951,
    "imperial tablespoons": 56.3121,
    "imperial teaspoons": 168.936,
    "us gallons": 0.264172,
    "us quarts": 1.05669,
    "us pints": 2.11338,
    "us cups": 4.22675,
    "us fluid ounces": 33.814,
}


# Loop until the user enters valid input
while True:
    # Prompt the user to choose the type of conversion they want to perform
    print("What type of conversion do you want to perform?")
    print("1. Distance")
    print("2. Temperature")
    print("3. Weight")
    print("4. Time")
    print("5. Volume")
    conversion_type = input("Enter the number of your choice: ")

    # Check if the user entered a valid conversion type
    if conversion_type not in ["1", "2", "3", "4", "5"]:
        print("\nInvalid input. Please try again.\n")
        continue

    # Show a list of available units for the chosen conversion type
    if conversion_type == "1":
        print("\nAvailable units for distance conversion:")
        for unit in distance_conversions.keys():
            print(unit)
    elif conversion_type == "2":
        print("\nAvailable units for temperature conversion:")
        for unit in temperature_conversions.keys():
            print(unit)
    elif conversion_type == "3":
        print("\nAvailable units for weight conversion:")
        for unit in weight_conversions.keys():
            print(unit)
    elif conversion_type == "4":
        print("\nAvailable units for time conversion:")
        for unit in time_conversions.keys():
            print(unit)
    elif conversion_type == "5":
        print("\nAvailable units for volume conversion:")
        for unit in volume_conversions.keys():
            print(unit)

    # Prompt the user to choose the units to convert between
    unit1 = input("\nEnter the first unit: ")
    unit2 = input("Enter the second unit: ")

    # Check if the user entered valid units
    if conversion_type == "1":
        if unit1 not in distance_conversions.keys() or unit2 not in distance_conversions.keys():
            print("\nInvalid units. Please try again.\n")
            continue
    elif conversion_type == "2":
        if unit1 not in temperature_conversions.keys() or unit2 not in temperature_conversions.keys():
            print("\nInvalid units. Please try again.\n")
            continue
    elif conversion_type == "3":
        if unit1 not in weight_conversions.keys() or unit2 not in weight_conversions.keys():
            print("\nInvalid units. Please try again.\n")
            continue
    elif conversion_type == "4":
        if unit1 not in time_conversions.keys() or unit2 not in time_conversions.keys():
            print("\nInvalid units. Please try again.\n")
            continue
    elif conversion_type == "5":
        if unit1 not in volume_conversions.keys() or unit2 not in volume_conversions.keys():
            print("\nInvalid units. Please try again.\n")
            continue

    # Look up the conversion factors for the chosen units
    if conversion_type == "1":
        factor1 = distance_conversions[unit1]
        factor2 = distance_conversions[unit2]
    elif conversion_type == "2":
        factor1 = temperature_conversions[unit1]
        factor2 = temperature_conversions[unit2]
    elif conversion_type == "3":
        factor1 = weight_conversions[unit1]
        factor2 = weight_conversions[unit2]
    elif conversion_type == "4":
        factor1 = time_conversions[unit1]
        factor2 = time_conversions[unit2]
    elif conversion_type == "5":
        factor1 = volume_conversions[unit1]
        factor2 = volume_conversions[unit2]

    # Prompt the user to enter the value to convert
    value = float(input("\nEnter the value to convert: "))

    # Perform the conversion
    converted_value = value * factor1 / factor2

    # Output the result
    print(f"{value} {unit1} is {converted_value} {unit2}\n")

    # Prompt the user to exit the program
    exit = input("Do you want to exit the program? (y/n) ")
    if exit.lower() == "y":
        break
