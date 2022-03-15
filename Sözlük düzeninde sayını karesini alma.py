#Verilen sayının karesini alıp sözlük düzeninde yazan python programı.
a=int(input("Bir sayı giriniz: "))
b=dict()
for i in range(1,a+1):
    b[i]=i*i
print(b)
