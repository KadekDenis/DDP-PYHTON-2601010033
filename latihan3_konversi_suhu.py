# konversi Celsius ke Fahrenheit dan Kelvin

# Input suhu dalam Celsius dari pengguna
celsius = float(input("Masukkan suhu dalam Celsius (°C): "))

# Rumus Konversi Suhu
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

# Menampilkan hasil konversi
print("\n=== HASIL KONVERSI SUHU ===")
print(f"Celsius    : {celsius:.2f} °C")
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")