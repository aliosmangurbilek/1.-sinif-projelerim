#ali osman alperen gürbilek 200312021
#boy ve kilo değişkenlerini tanımladım.
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
 #indeksi hesapladım
indeks  = kilo/(boy**2)
 #if elif else koşullu ifadeleri kullandım 
if indeks <18.5:
    print('zayif Vucut Kitle Indeksi:{}'.format(round(indeks)))
elif indeks >= 18.5 and indeks <24.9 :
    print('normal Vucut Kitle Indeksi:{}'.format(round(indeks)))
elif indeks >= 24.9 and indeks <29.9:
    print('kilolu Vucut Kitle Indeksi:{}'.format(round(indeks)))
elif indeks >= 29.9 and indeks <=34.9:
    print('obez Vucut Kitle Indeksi:{}'.format(round(indeks)))
else:
    print('ciddi obez Vucut Kitle Indeksi:{}'.format(round(indeks)))
#Format komutu string bir ifadenin içine değişken eklememize yardımcı olur.
#Round komutu ondalıklı herhangi bir sayıyı en yakın tam sayıya yuvarlar.