#Ali Osman Alperen Gürbilek 200312021
#kullanıcıdan maaş bilgisi ve maaşının yüzde kaçını biriktirmek istediğini öğrenelim.

maas = int(input('Lütfen maaşınızı giriniz(TL):'))
maasin_yuzdesi = int(input('Maaşınızın yüzde kaçını biriktirmek istersiniz(%):'))

#hesaplamayı matematiksel olarak yaptım.
maas * maasin_yuzdesi/100

#ev fiyatını belirledim.
ev_fiyatı=500000

#tekrar matematiksel hesaplama yaptım.
kac_ay_lazim = (500000//(maas*maasin_yuzdesi/100))
metin='Evi almak için {} aya ihtiyacınız vardır'

#ifadeye metin eklmek için .format komutunu kullandım.
print(metin.format(kac_ay_lazim))