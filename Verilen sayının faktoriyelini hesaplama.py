#Verilen sayıların faktöriyelini hesaplayan bir program yazınız. Sonuçlar, tek bir satırda virgülle ayrılmış bir sırayla yazdırılmalıdır. Programa aşağıdaki girdinin sağlandığını varsayalım: 8 O zaman çıktı şöyle olmalıdır: 40320
x = int(input("bir sayı giriniz "))
def faktoriyel (x):
    if x == 0 :
        return 1
    return x * faktoriyel(x - 1) 
print (faktoriyel(x))