n = int(input("Bir sayı girin: "))

toplam = 0

for i in range(1, n+1):
    toplam += i

print(f"1'den {n} sayısına kadar olan sayıların toplamı: {toplam}")