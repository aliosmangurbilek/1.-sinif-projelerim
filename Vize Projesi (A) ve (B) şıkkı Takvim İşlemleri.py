
#Ali Osman Alperen Gürbilek 200312021


#(A) ŞIKKI:

#Deneme Kodları:
# (1, 12, 2021, 0, 4, 12, 2021, 23) verildi˘ginde “95 saat vardır.” ¸cıktısını vermelidir.
# (1, 12, 1990, 0, 1, 12, 2021, 18) verildi˘ginde “271770 saat vardır.” ¸cıktısını vermelidir

#Artık yıl hesap eden fonksiyonum.
def artik_yil (yil):
    if yil % 400 == 0 :
        return True
    if yil % 100 == 0 :
        return False 
    if yil % 4 == 0 :
        return True
    return False

#Aylarda kaç gün olduğunu hesap eden fonksiyonum.
def ay_gunleri (yil,ay):
    if ay == 1 or ay == 3 or ay == 5 or ay == 7 \
        or ay == 8 or ay == 10 or ay == 12 :
        return 31
    else:
        if ay == 2:
            if artik_yil(yil):
                return 29
            else:
                return 28 
        else:
            return 30

#Yılın içindeki gün sayısını hesap eden fonksiyonum.
def yilin_gun_adedini_bul(yil, ay, gun):
    gun_sayisi = 0

    #yılların içindeki gün sayısını hesap ediyoruz.
    for x in range(1900, yil + 1):
        if(artik_yil(x)):
            gun_sayisi = gun_sayisi + 366
        else:
            gun_sayisi = gun_sayisi + 365
    #ayların içindeki gün sayısını hesap ediyoruz.
    for x in range(1, ay):
        gun_sayisi = gun_sayisi + ay_gunleri(yil, x)
    #günleri hesap ediyoruz. 
    gun_sayisi = gun_sayisi + gun
    return gun_sayisi

#İnput fonksiyonu ile bilgileri aldım.
tarih = input("Lütfen tarih giriniz: ")

#Girilen string değeri kullanabilmek için listeye attım.
son_tarih = tarih.split(",")

#Girilen 1. Tarihin listedeki elemanlarını kullandım.
gun1 = int(son_tarih[0])
ay1 = int(son_tarih[1])
yil1 = int(son_tarih[2])
saat1 = int(son_tarih[3])

#Girilen 2. Tarihin listedeki elemanlarını kullandım.
gun2 = int(son_tarih[4])
ay2= int(son_tarih[5])
yil2 = int(son_tarih[6])
saat2 = int(son_tarih[7])

#Yilin_gun_adedi prosedüründen çıkan bilgileri kullanabilmek için değişkene atadım.
ilk_gun_adedi = yilin_gun_adedini_bul(yil1, ay1, gun1)
ikinci_gun_adedi = yilin_gun_adedini_bul(yil2, ay2, gun2)

#Girilen iki tarih arası farkı hesapladım.
fark_gun = ikinci_gun_adedi - ilk_gun_adedi
hafta_sayisi = int(fark_gun / 7)
fark_saat = 0

#Eğer saat1 > saat2'den ise algoritmanın nasıl elde alacağının kodunu yazdım.
if(saat1 > saat2):
    fark_gun = fark_gun - 1
    saat1 = saat1 + 24 
    fark_saat = saat2 - saat1
else:
    fark_saat = saat2 - saat1

fark_saat = fark_saat + fark_gun * 24

#Print fonkiyonunu kullanarak ekrana istenilen bilgiyi yazdırdım.
sonuc = (str(fark_saat)) + " Saat vardır."
print(sonuc)






#(B) ŞIKKI:

#Deneme kodları:
# (1, 1, 2020, 31, 12, 2020, [“Salı”, “pazar”]) verildiğinde
#“52 tane salı günü vardır.”
#“53 tane pazar günü vardır.” çıktısını vermelidir.
#1, 1, 1900, 25, 12, 2021, [“Cumartesi”]
#6365 tane Cumartesi günü vardır çıktısını vermelidir.

#Artık yıl hesap eden fonksiyonum.
def artik_yil (yil):
    if yil % 400 == 0 :
        return True
    if yil % 100 == 0 :
        return False 
    if yil % 4 == 0 :
        return True
    return False

#Aylarda kaç gün olduğunu hesap eden fonksiyonum.
def ay_gunleri (yil,ay):
    if ay == 1 or ay == 3 or ay == 5 or ay == 7 \
        or ay == 8 or ay == 10 or ay == 12 :
        return 31
    else:
        if ay == 2:
            if artik_yil(yil):
                return 29
            else:
                return 28 
        else:
            return 30

#Yılın içindeki gün sayısını hesap eden fonksiyonum.
def yilin_gun_adedini_bul(yil, ay, gun):
    gun_sayisi = 0

    #yılların içindeki gün sayısını hesap ediyoruz.
    for x in range(1900, yil + 1):
        if(artik_yil(x)):
            gun_sayisi = gun_sayisi + 366
        else:
            gun_sayisi = gun_sayisi + 365
    #ayların içindeki gün sayısını hesap ediyoruz.
    for x in range(1, ay):
        gun_sayisi = gun_sayisi + ay_gunleri(yil, x)
    #günleri hesap ediyoruz. 
    gun_sayisi = gun_sayisi + gun

    return gun_sayisi

#İnput fonksiyonu ile kullanıcıdan bilgi aldım.
tarih = input("Lütfen tarih giriniz: ")

#Girilen string değeri parse edebilmek için listeye atıyoruz.
son_tarih = tarih.split(",")

#Girilen 1. Tarihin listedeki elemanlarını kullandım.
gun1 = int(son_tarih[0])
ay1 = int(son_tarih[1])
yil1 = int(son_tarih[2])

#Girilen 2. Tarihin listedeki elemanlarını kullandım.
gun2 = int(son_tarih[3])
ay2= int(son_tarih[4])
yil2 = int(son_tarih[5])

#İnputla aldığım bilgiyi boş listeye attım. 
#Daha sonra for döngüsü ile listenin uzunluğunu hesap ettim.
istenen_gunler = []
for x in range(len(son_tarih) - 6):
    istenen_gunler.append(son_tarih[x + 6])
    
#Yilin_gun_adedi prosedüründen çıkan bilgileri kullanabilmek için değişkene atadım.
ilk_gun_adedi = yilin_gun_adedini_bul(yil1, ay1, gun1)
ikinci_gun_adedi = yilin_gun_adedini_bul(yil2, ay2, gun2)

#Girilen iki tarih arası farkı hesapladım.
fark_gun = ikinci_gun_adedi - ilk_gun_adedi
hafta_sayisi = int(fark_gun / 7)

#Başka bir for döngüsü ile listeye attığımız elemanları kullandım.
#Print fonksiyonu ile ekrana yazdırdım. 
for x in range (len(istenen_gunler)):
    sonuc = str(hafta_sayisi + 1) + "tane " + istenen_gunler[x] + " günü vardır."
    print(sonuc)

