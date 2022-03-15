bos = []
list= [1, 2, 34, 45, 56, 67, 89]
def karesini_al():
    for i in range(len(list)):
        kare = i * i
        bos.append(kare)
karesini_al()
print(bos)

list.sort(reverse= True)
print(list)