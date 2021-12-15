#ALİ OSMAN ALPEREN GÜRBİLEK 200312021
#cümleyi cümle isimli değişkene atadım.
cumle="Bilim hepimizi eğlendirebilir ve büyüleyebilir ancak dünyayı değiştiren mühendisliktir."
#cümledeki boşluk sayısını buldum.
kac_tane_bosluk_var=cumle.count(' ')
#indise 0 verdim 0'dan başlaması için.
indis=0
#boşluk sayısının bir fazlası kelime sayısı olacağından boşluk sayısına 1 ekledim.
bosluk_sayisi = (int(kac_tane_bosluk_var+1))
#.format komutu ile metin içine sayı ekledim.
metin = "cümle {} kelimeden oluşmuştur."
#print komutu ile ekrana istenilen değeri yazdırdım.
print(metin.format(bosluk_sayisi))