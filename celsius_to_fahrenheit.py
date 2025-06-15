def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Take user input
c = float(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)

print(f"{c}°C is equal to {f:.2f}°F")
