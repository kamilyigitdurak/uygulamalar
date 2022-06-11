sayı = int(input("Faktöriyeli Hesaplanacak Sayıyı Giriniz :"))
factorıal = 1
for x in range(1,sayı+1):
    factorıal *= x
print("{} sayısının faktöriyeli :{}".format(sayı,factorıal))
