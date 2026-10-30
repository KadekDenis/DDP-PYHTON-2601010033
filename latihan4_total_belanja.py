# menghitung total belanja dengan PPN 11%

subtotal = float(input("Masukkan total harga belanja (Rp): "))

PPN_PERSEN = 0.11
nominal_ppn = subtotal * PPN_PERSEN
total_bayar = subtotal + nominal_ppn

print("\n=== RINCIAN TOTAL BELANJA ===")
print(f"Subtotal Belanja : Rp {subtotal:,.2f}")
print(f"PPN (11%)        : Rp {nominal_ppn:,.2f}")
print(f"Total Bayar      : Rp {total_bayar:,.2f}")