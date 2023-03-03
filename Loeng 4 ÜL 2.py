#Arvu arvamise mäng
#lase arvutil valida suvaline arv mingis vahemikus ja mängijal pakkuda
#peale pakkumist peab programm ütlema, kas õige arv on suurem või väiksem
import random
arvuti_arv = random.randint(1,100)
pakkumised = 0
Mängija_arv = int(input("Mis sa pakud?"))
while Mängija_arv != arvuti_arv and pakkumised < 7:
    if Mängija_arv < arvuti_arv:
        Mängija_arv = int(input("Paku uuesti! Õige arv on suurem."))
        pakkumised = pakkumised +1
    else:
        Mängija_arv = int(input("Paku uuesti! Õige arv on väiksem"))
        pakkumised = pakkumised +1
if Mängija_arv == arvuti_arv:
    print("Arvasid ära!")
else:
    print("Kahjuks said katsed otsa. Sa kaotasid.")
                 

                 