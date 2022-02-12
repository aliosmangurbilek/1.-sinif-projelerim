kelime="Karşında ziya yoksa, sağından ya solundan Tek bir ışık olsun buluver, kalma yolundan."
sayac=0
while sayac < len(kelime.split()):
    print (kelime.split()[sayac])
    sayac=sayac+1
sesli_harfler = 'AEIİOÖUÜaeıioöuü'
sayac = 0
for i in kelime:
    if i in sesli_harfler:
        sayac += 1
print((sayac))
print(kelime[::-1])
