ilksayı = int(input("İlk Sayıyı Giriniz:"))
sonsayı = int(input("Son Sayıyı Giriniz:"))
toplam = 0
for x in range(ilksayı,sonsayı+1):
    toplam += x
print(toplam)