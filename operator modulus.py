# Contoh 1: Mengetahui apakah suatu bilangan habis dibagi bilangan lain
bilangan = 15
pembagi = 5

if bilangan % pembagi == 0:
    print(bilangan, "habis dibagi", pembagi)
else:
    print(bilangan, "tidak habis dibagi", pembagi)

# Output: 15 habis dibagi 5

# Contoh 2: Mengetahui digit paling kanan suatu bilangan
bilangan = 12345
digit_terakhir = bilangan % 10
print("Digit paling kanan dari", bilangan, "adalah", digit_terakhir)

# Output: Digit paling kanan dari 12345 adalah 5



# Contoh: Menggandakan string dengan operator *
string_awal = "Hello"
kali = 3
string_gandakan = string_awal * kali
print(string_gandakan)

# Output: HelloHelloHello
