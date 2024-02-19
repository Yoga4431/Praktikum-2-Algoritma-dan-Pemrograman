# Alur kerja: Input - Proses - Output

# Input: Meminta pengguna untuk memasukkan kartu ATM
input("Masukkan kartu ATM Anda dan tekan Enter: ")

# Input: Meminta pengguna untuk memasukkan PIN
pin = input("Masukkan PIN Anda: ")

# Proses: Melakukan proses pengecekan PIN
if pin == "1234":
    print("PIN Anda benar. Silakan lanjutkan transaksi.")
else:
    print("PIN Anda salah. Transaksi ditolak.")
    exit()  # Keluar dari program jika PIN salah

# Proses: Melakukan proses penarikan uang
jumlah_penarikan = float(input("Masukkan jumlah uang yang ingin ditarik (dalam Rupiah): "))

# Output: Mengeluarkan uang sesuai dengan jumlah yang diminta
print("Silakan ambil uang Anda sejumlah Rp.", jumlah_penarikan)

# Output: Memberikan bukti penarikan
print("Terima kasih telah menggunakan layanan ATM kami. Simpan baik-baik bukti transaksi Anda.")
