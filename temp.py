
temp = float(input("Enter temperature in °C: "))

if temp < 20:
    status = "Cold"
elif 20 <= temp <= 30:
    status = "Normal"
else:
    status = "Hot"

print("Temperature:", temp, "°C")
print("Status:", status)

#added farenheit conversion.
temp_f = (temp_c * 9/5) + 32
print("Temperature in Fahrenheit:", round(temp_f, 2), "°F")