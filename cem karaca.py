#Ali Osman Alperen Gürbilek 200312021
aliosman = '\
Bugün sen çok gençsin yavrum\
Hayat ümit, neşe dolu\
Mutlu günler vaad ediyor\
Sana yıllar ömür boyu\
\
\
Ne yalnızlık ne de yalan üzmesin seni\
Doğarken ağladı insan\
Bu son olsun, bu son\
Doğarken ağladı insan\
Bu son olsun, bu son\
\
\
Bugün sen çok gençsin yavrum\
Hayat ümit, neşe dolu\
Mutlu günler vaad ediyor\
Sana yıllar ömür boyu\
\
\
Ne yalnızlık ne de yalan üzmesin seni\
Doğarken ağladı insan\
Bu son olsun, bu son\
Doğarken ağladı insan\
Bu son olsun, bu son\
Ne yalnızlık ne de yalan üzmesin seni\
Doğarken ağladı insan\
Bu son olsun, bu son\
Doğarken ağladı insan\
Bu son olsun, bu son'
#string adedi değişkenine aliosman değişkenini atadım ve count komutuyla kaç edet 'son' olduğunu buldum.
string_adet=aliosman.count('son')
#indise 0 verdim 0'dan başlaması için.
indis=0
print(string_adet)
#range komutu ile  belirli aralıkdakı sayıları kullanmak için kullanılır.
#for döngüsü kullanarak yazdım kodu.
for x in range(string_adet):
    bulunan_indis = aliosman.find('son', indis + 1)
#find komutu ile 'son' ları buldum.
    indis = bulunan_indis
#bulduğumuz indisi tekrar döngüye soktum.
    print (bulunan_indis)
    
    
    
 
