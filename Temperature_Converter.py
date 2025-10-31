# temperature_converter.py

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

print("Temperature Converter:")
print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Celsius to Kelvin\n4. Kelvin to Celsius")

choice = input("Enter choice (1-4): ")

temp = float(input("Enter temperature value: "))

if choice == '1':
    print(f"{temp}°C = {c_to_f(temp):.2f}°F")
elif choice == '2':
    print(f"{temp}°F = {f_to_c(temp):.2f}°C")
elif choice == '3':
    print(f"{temp}°C = {c_to_k(temp):.2f}K")
elif choice == '4':
    print(f"{temp}K = {k_to_c(temp):.2f}°C")
else:
    print("Invalid choice.")
