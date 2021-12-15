#ALİ OSMAN ALPEREN GÜRBİLEK 200312021
kelime="hanımeli"
#format fonksiyonu ile kelimelere cümle ekledim.
metin="esas kelime:{}"
print(metin.format(kelime))
#format fonksiyonu ile kelimelere cümle ekledim.
ilk_kisim="hanı"
ikinci_kisim="meli"
#format fonksiyonu ile kelimelere cümle ekledim.
metin1="kelimenin birinci kısmı:{}"
print(metin1.format(ilk_kisim))
#format fonksiyonu ile kelimelere cümle ekledim.
metin2="kelimenin ikinci kısmı:{}"      
print(metin2.format(ikinci_kisim))

#for döngüsü ile kelimenin uzunluğunu buldum.
uzunluk=0
for x in kelime:
  uzunluk=uzunluk+1
 
kelimenin_yarisi=((uzunluk//2)-1)
#başka bir for döngüsü ile 'hey' kelimesinin kelimenin ortasına ekledim.
indis=0 
ilk_kisimf=""
for x in range(uzunluk):
    ilk_kisimf=ilk_kisimf + kelime[indis]
    if indis==kelimenin_yarisi:
        ilk_kisimf=ilk_kisimf + "hey"
    indis=indis+1  
#tekrar format fonksiyonu ile ekranı cümleyi yazdırdım.
metin3="yeni kelime:{}"         
print(metin3.format(ilk_kisimf))