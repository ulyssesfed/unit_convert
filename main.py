# Define a dictionary of conversion factors for distance units
distance_conversions = {
    "millimeters": 1000,
    "centimeters": 100,
    "meters": 1,
    "kilometers": 0.001,
    "inches": 39.3701,
    "feet": 3.28084,
    "yards": 1.09361,
    "miles": 0.000621371
}

# Define a dictionary of conversion factors for temperature units
temperature_conversions = {
    "celsius": 1,
    "fahrenheit": 9/5,
    "kelvin": -273.15
}

# Loop until the user enters valid input
while True:
    # Prompt the user to choose the type of conversion they want to perform
    print("What type of conversion do you want to perform?")
    print("1. Distance")
    print("2. Temperature")
    conversion_type = input("Enter the number of your choice: ")

    # Check if the user entered a valid conversion type
    if conversion_type not in ["1", "2"]:
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

    # Look up the conversion factors for the chosen units
    if conversion_type == "1":
        factor1 = distance_conversions[unit1]
        factor2 = distance_conversions[unit2]
    elif conversion_type == "2":
        factor1 = temperature_conversions[unit1]
        factor2 = temperature_conversions[unit2]

    # Prompt the user to enter the value to convert
    value = float(input("\nEnter the value to convert: "))

    # Perform the conversion
    converted_value = value * factor1 / factor2

    # Output the result
    print(f"{value} {unit1} is {converted_value} {unit2}\n")
