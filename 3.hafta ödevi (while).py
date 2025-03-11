n = int(input("Bir sayı girin: "))

toplam = 0
i = 1

while i <= n:
    toplam += i
    i += 1

print(f"1'den {n} sayısına kadar olan sayıların toplam:{toplam}")