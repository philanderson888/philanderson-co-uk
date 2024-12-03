# Unit Converter: (temp , currency, volume) Converts various units between one another.
#  The user enters the type of unit being entered, the type of unit they want to convert to and then the value. 
# The program will then make the conversion
# Temp (Degress to Farenheight), currency (GBP to dollars), volume (Litres to gallons)
choice = input("Type C to convert from Celcius to Fahrenheit, and F to convert from Fahrenheit to Celcius:")
if choice == "C":
    celcius = float(input("Enter the temperature in Degrees:   "))
    conversion = (celcius * 9/5) + 32
    print(f"{conversion} Degrees Fahrenheit")

if choice == "F":
    faren = float(input("Enter the temperature in Fahrenheit:   "))
    conversion2 = (faren - 32) * 5/9
    print(f"{conversion2} Degrees celcius")