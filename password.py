secimSayi = int(input("Şifrenizi giriniz: "))
#Kullanıcıdan input fonksiyonu ile şifresini girmesini istedim.
#Daha sonra başka bir fonksiyon ile istenilen seçimleri ve çıktıları verdim.
def password(secim):
    secimList = [int(x) for x in str(secim)]
#for döngüsü ile kullanıcının girdiği şifreyi liste haline getirdim ve gerekli işlemleri yaptım.    
    if secim > 99 and secim < 1000:
        if secimList[0] > secimList[1] and secimList[1] > secimList[2] and secim%2 == 0:
            print("güçlü şifre")   
        elif secimList[0] != secimList[1] and secimList[0] != secimList[2] and secimList[1] != secimList[2] and secim%2 == 0: 
            print("orta düzeyde şifre")
        elif secim%2 == 0:
            print("zayıf şifre")
        elif secim%2 == 1:
            print("bu şifre kullanılamaz")
    else:
        print("geçersiz şifre")
        
password(secimSayi)