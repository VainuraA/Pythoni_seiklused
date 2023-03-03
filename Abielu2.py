fail_sisse = open("haridus.txt", "r", encoding = "utf-8")

kohad = list()
liik = list()
koik_mehed = list()
koik_naised = list()
abimehed = list()
abinaised = list()

for rida in fail_sisse:
    ajutine = rida.split()
    kohad.append(ajutine[0])
    liik.append(ajutine[1])
    koik_mehed.append(int(ajutine[2]))
    koik_naised.append(int(ajutine[3]))
    abimehed.append(int(ajutine[4]))
    abinaised.append(int(ajutine[5]))
fail_sisse.closed

mitu = len(kohad)
koguabi = 0
kogupop = 0

for i in range(mitu):
    koguabi = abimehed[i]+ abinaised[i] + koguabi
    kogupop = koik_naised[i] + koik_mehed[i] + kogupop
protsent = (koguabi/kogupop)*100
print("2019 abiellus", koguabi, "inimest, mis moodustas populatsioonist", round(protsent, 1))

loendur = 0

for i in range(mitu):
    if liik[i] == "vald":
        valla_protsent = (abimehed[i]+abinaised[i])/(koik_mehed[i]+koik_naised[i])*100
        if valla_protsent > protsent:
            loendur = loendur + 1
print("Abiellunute protsent oli Eesti protsendist suurem", loendur, "vallas")
    
sisestatud = int(input("Sisesta arv, millega tahad võrrelda"))
indeksid = list()

for i in range(mitu):
    erinevused = abs(abimehed[i]-abinaised[i])
    if erinevused > sisestatud:
        indeksid.append(i)
mitu2 = len(indeksid)
if mitu2 > 0:
    for i in range(mitu2):
        print()
        print("%3s" % (kohad[indeksid[i]]), "%3s" % (liik[indeksid[i]]))
else:
    print("Selliseid pole")