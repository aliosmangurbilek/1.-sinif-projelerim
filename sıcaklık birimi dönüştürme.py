secimString = input("Değeri giriniz: ")
#İnput fonksiyonu ile kullanıcıdan bilgi aldım.
#Fonksiyona input değerini soktum.
#Gerekli hesaplamaları gerçekleştirdim. 
def heat_unit(secim):
#split fonksiyonu ile girilen input değerini iki kısma ayırdım. integer kısmını işlemlerde kullandım ve gerekli işlemleri gerçekliştirdim.
    sayi = secim.split(" ");
    if sayi[1] == "Celsius":
        fahrenheit=(int((sayi[0])*9)+160)/5.0
        print("Fahrenheit: ",fahrenheit)   
    elif sayi[1] == "Fahrenheit":
        celc=(int((sayi[0])*5)-160)/9.0
        print("Celsius: ",celc)   
    elif sayi[1] == "Kelvin":
        reaumur=(int((sayi[0])*4)-1092)/5.0
        print("Reaumur: ",reaumur)   
    elif sayi[1] == "Reaumur":
        Reaumur=(int((sayi[0])*5)+1092)/4.0
        print("Kelvin: ",Reaumur)   
        
heat_unit(secimString)