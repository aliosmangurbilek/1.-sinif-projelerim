liste_corba = ["mercimek çorbası","ezogelin çorbası"]
liste_anayemek = ["köfte","mantı","karnıyarık","fasulye"]
liste_sogukluk = ["cacık","salata","ezme"]
liste_icecek = ["kola","meyve suyu","ayran"]
#Ayrı ayrı menüdeki değerleri listeler halinde yazdım.
#İşlemlerimde girilen inputların liste değerlerini kullandım. 
#İnputları istek değişkenlerine integer olarak atadım.  
istek_corba = int((input("Kaç numaralı çorbayı istersiniz? ")))
istek_anayemek = int((input("Kaç numaralı ana yemeği istersiniz? ")))
istek_sogukluk = int((input("Kaç numaralı soğukluğu istersiniz? ")))
istek_icecek =int((input("Kaç numaralı içeceği istersiniz? ")))
#Daha sonra bir fonksiyon kullanarak kullanıcının inputlarını işledim.
#/n komutunu, print komutunu alt alta yazdırmak için kullandım.
#Or operatörünü kullandım daha sonra.   
def take_order(secim_corba,secim_anayemek,secim_sogukluk,secim_icecek):
    if  secim_corba == 1 or secim_corba == 2 :
        print("Çorba : " + liste_corba[secim_corba - 1] + "\n")
    else:pass
    if  secim_anayemek == 1 or secim_anayemek == 2 or secim_anayemek == 3 or secim_anayemek == 4 :
        print("Ana Yemek : " + liste_anayemek[secim_anayemek - 1] + "\n")
    else:pass
    if  secim_sogukluk == 1 or secim_sogukluk == 2 or secim_sogukluk == 3:
        print("Soğukluk : " + liste_sogukluk[secim_sogukluk - 1] + "\n")
    else:pass
    if  secim_icecek == 1 or secim_icecek == 2 or secim_icecek == 3:
        print("İçecek : " + liste_icecek[secim_icecek - 1] + "\n")
    else:pass

take_order(istek_corba,istek_anayemek,istek_sogukluk,istek_icecek)

print('Sipariş edildi')
        
    