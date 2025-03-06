# Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı girin: "))

# Negatif sayı kontrolü
if sayi < 0:
    print("Negatif sayı girdiniz!")
else:
    # Sayının çift mi tek mi olduğunu kontrol et
    if sayi % 2 == 0:
        print(f"{sayi} bir çift sayıdır.")
    else:
        print(f"{sayi} bir tek sayıdır.")

