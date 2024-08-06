# Program to convert Temperatures
# Supported Conversions include Celsius, Fahrenheit, and Kelvin

print("Temperature Converter\n")

print("""
1. Celsius
2. Fahrenheit
3. Kelvin
""")

# Taking user inputs and conversions
scale_in_use = int(input("Enter the scale currently in use (1/2/3): "))
scale_to_convert = int(input("Type to convert to another scale (1/2/3): "))
user_input_value = float(input("Enter the value of the conversion: "))

# checking for error and evaluating the results
if scale_in_use == scale_to_convert:
    print("Error! cant convert to the same scale.")
elif scale_in_use >=4 or scale_to_convert >= 4:
    print("Error!! check typing!")
else:
    print("Your Converted Output is:")
    if scale_in_use == 1:
        if scale_to_convert == 2:
            # Celsius to Fahrenheit
            converted_to_Fahrenheit = (user_input_value * 9/5) + 32
            print(converted_to_Fahrenheit,"F")
        elif scale_to_convert == 3:
            # Celsius to Kelvin
            converted_to_Kelvin = user_input_value + 273.15
            print(converted_to_Kelvin,"K")
    elif scale_in_use == 2:
        if scale_to_convert == 1:
            # Fahrenheit to Celsius
            converted_to_Celsius = (user_input_value - 32) * 5/9
            print(converted_to_Celsius,"C")
        elif scale_to_convert == 3:
            # Fahrenheit to Kelvin
            converted_to_Kelvin = (user_input_value + 459.67) * 5/9
            print(converted_to_Kelvin,"K")
    elif scale_in_use == 3:
        if scale_to_convert == 1:
            # Kelvin to Celsius
            converted_to_Celsius = user_input_value - 273.15
            print(converted_to_Celsius,"C")
        elif scale_to_convert == 2:
            # Kelvin to Fahrenheit
            converted_to_Fahrenheit = (user_input_value * 9/5) - 459.67
            print(converted_to_Fahrenheit,"F")
