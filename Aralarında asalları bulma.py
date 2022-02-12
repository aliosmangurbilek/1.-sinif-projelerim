#Ali Osman Alperen Gürbilek 200312021
x = int(input("Sayı 1: "))
y= int(input("Sayı 2: "))
def bolunenleri_bul(x,y):
    i = 1
    while i < 100:
        i =i + 1
        if i%x==0 and i%y==0 : 
            pass
        elif i%x==0 or i%y==0:
            print(i)
        else:
            None    
bolunenleri_bul(x,y)