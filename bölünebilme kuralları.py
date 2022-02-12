#2000 ile 3200 (her ikisi de dahil) arasında 7 ile bölünebilen ancak 5'in katı olmayan tüm sayıları bulan bir program yazın. Elde edilen sayılar tek satırda virgülle ayrılmış şekilde basılmalıdır.
bos = []
for i in range (2000, 3201):
    if i % 7 == 0 and i % 5 != 0 :
        bos.append(i)
print(bos)