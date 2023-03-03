# Tekstifailis haridus.txt on andmed rahvastiku hariduse kohta erinevates linnades ja valdades. Ühes reas on valla 
# või linna nimi, üksuse liik, kõrghardusega meeste arv, meeste koguarv, kõrghardusega naiste arv ja naiste koguarv 
# (positiivsed täisarvud). Võib eeldada, et fail vastab kirjeldusele. 
# Leida omavalitsus, kus on suurim kõrgharidusega meeste protsent meeste koguarvust. Trükkida välja omavalitsuse nimi, 
# liik ja protsent. 
# Loendada, mitmes linnas on kõrghariduseta naisi rohkem kui mehi.
# Trükkida tabel nende omavalitsusüksuste andmetega (nimi, liik, kõrgharidusega inimeste arv), kus kõrgharidusega 
# inimeste arv on suurem mingist etteantud suurusest. Viimase sisestab kasutaja. Kui selliseid omavalitsusi ei ole, 
# anda sobilik teade.

fail_sisse = open("haridus.txt", "r", encoding = "utf-8")

kohad = list()
liik = list()
korg_mehed= list()
mehed = list()
korg_naised = list()
naised = list()

for rida in fail_sisse:
    ajutine = rida.split()
    kohad.append(ajutine[0])
    liik.append(ajutine[1])
    korg_mehed.append(int(ajutine[2]))
    mehed.append(int(ajutine[3]))
    korg_naised.append(int(ajutine[4]))
    naised.append(int(ajutine[5]))
fail_sisse.close()

mitu = len(korg_mehed)
protsent = 0

for i in range(mitu):
    uus_protsent = (korg_mehed[i] / mehed[i])*100
    if uus_protsent > protsent:
        protsent = uus_protsent
        indeks = i
print("Kõige rohkem:", kohad[indeks], liik[indeks], round(protsent, 1), "%")

loendur = 0

for i in range(mitu):
    khariduseta_naine = naised[i] - korg_naised[i]
    khariduseta_mees = mehed[i] - korg_mehed[i]
    if khariduseta_naine > khariduseta_mees:
        loendur = loendur + 1
        
print(loendur, "linnas on kõrghariduseta naisi rohkem kui mehi")

etteantud_suurus = int(input("Sisesta suurus, mida tahad võrrelda "))
koik_korg = list()
korgarvud = list()

for i in range(mitu):
    kogu_korg = korg_mehed[i]+ korg_naised[i]
    if kogu_korg > etteantud_suurus:
        koik_korg.append(i)
        korgarvud.append(kogu_korg)

mitu2 = len(koik_korg)


if mitu2 > 0:
    for i in range(mitu2):
        print()
        print("%3s" % (kohad[koik_korg[i]]), "%3s" % (liik[koik_korg[i]]), "%3s" % (korgarvud[i]))
        print()
else:
    print("Selliseid omavalitsusi ei ole.")
        