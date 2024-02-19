def hitung_berat_badan(tinggi_badan, bmi_harapan):
    """
    Fungsi untuk menghitung berat badan yang dibutuhkan berdasarkan tinggi badan
    dan nilai Indeks Massa Tubuh (BMI) yang diharapkan.
    
    Parameters:
    tinggi_badan (float): Tinggi badan dalam satuan meter.
    bmi_harapan (float): Nilai BMI yang diharapkan.
    
    Returns:
    float: Berat badan yang dibutuhkan untuk mencapai BMI yang diharapkan.
    """
    berat_badan = bmi_harapan * tinggi_badan**2
    return berat_badan

def main():
    # Input tinggi badan dari pengguna
    tinggi_badan = float(input("Masukkan tinggi badan Anda (dalam meter): "))

    # Input nilai BMI yang diharapkan
    bmi_harapan = float(input("Masukkan nilai Indeks Massa Tubuh (BMI) yang diharapkan: "))

    # Hitung berat badan yang dibutuhkan
    berat_badan_dibutuhkan = hitung_berat_badan(tinggi_badan, bmi_harapan)

    # Output hasil
    print("Berat badan yang dibutuhkan untuk mencapai BMI", bmi_harapan, "adalah:", berat_badan_dibutuhkan, "kg")

if __name__ == "__main__":
    main()
