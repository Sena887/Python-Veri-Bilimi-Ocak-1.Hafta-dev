def en_buyuk_en_kucuk_bul():
    sayilar = []
    for i in range(5):
        sayi = int(input(f"{i+1}. sayıyı girin: "))
        sayilar.append(sayi)

    en_buyuk = max(sayilar)
    en_kucuk = min(sayilar)

    print(f"En büyük sayı: {en_buyuk}")
    print(f"En küçük sayı: {en_kucuk}")

en_buyuk_en_kucuk_bul()