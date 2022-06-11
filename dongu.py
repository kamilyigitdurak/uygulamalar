# Asal Sayı Kontrol Programı
sayac = 0
sayı = int(input("Sayıyı Giriniz:"))
if sayı < 2:
    print("En Küçük Asal Sayı 2 dir.")
else:
    for x in range(2,sayı):
        if sayı % x == 0:
            sayac += 1
        else:
            continue
    if sayac != 0:
        print("Bu Sayı Asal Değildir.")
    else:
        print("Bu Sayı Asaldır.")