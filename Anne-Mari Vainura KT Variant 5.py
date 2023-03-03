#Programm küsib kasutajalt, mitu arvu programm tegema peab.
#Edasi genereerib programm juhuslikke täisarve.
#Trükib ekraanilearvud, mis jaguvad samaaegselt nii 3-ga kui ka 5-ga
#ning leiab nende aritmeetilise keskmise
#Lõpuks väljastab programm keskmise.
import random
Mitu = int(input("Mitu arvu peab programm tegema?"))
mitu = 0
arit_keskm = 0
mitu_jaguvat = 0
ARV = 0
while mitu != Mitu :
    arv = random.randint(0,100)
    mitu = mitu + 1
    if arv % 3 == 0 and arv % 5 == 0:
        print(arv)
        mitu_jaguvat = mitu_jaguvat + 1
        ARV = ARV + arv
        arit_keskm = ARV / mitu_jaguvat
    else:
        print(arv, "See ei sobi")
print("Leidsin ", Mitu, "arvu, milledest ", mitu_jaguvat, "jaguvad samaaegselt nii 3 kui ka 5-ga.")
print("Ning nende arvude aritmeetiline keskmine on ", arit_keskm)

    
