# konversi Celsius ke Fahrenheit dan Kelvin

celsius = float(input("Masukkan suhu dalam Celsius (°C): "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("\n=== HASIL KONVERSI SUHU ===")
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")