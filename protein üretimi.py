#ALİ OSMAN ALPEREN GÜRBİLEK 200312021
#kodu zincir adlı değişkene atadım.
zincir="UGGCUAUGUGGUUUGGCUCCUAGACAUACGAAUG"
#.find fonksiyonu ile başlangıç kodunu buldum.
baslangıc_kodu = zincir.find('AUG')
#aynı şekilde bitiş kodunu buldum. 
bitis_kodu=zincir.find("UAG")
#bitiş kodu - başlangıç kodu / 3 yaparak kaç tane protein sentezlendiğini buldum.
toplam_kodon=((int(bitis_kodu))-(int(baslangıc_kodu)))//3
#print komutu ile ekrana yazdırdım.
print(toplam_kodon)
