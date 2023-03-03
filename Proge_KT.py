# Ülesanne 3
# Tekstifailis kt_2.txt on ühe kuu temperatuurid ja kuupäevad, millal selline temperatuur esines.
# Täpsemalt on tekstifaili esimesel real kuupäevade arv ning igal järgneval real on kaks täisarvu: kuupäev ja temperatuur.
# Kirjutada programm nende päevade keskmise temperatuuri leidmiseks, kus kraadiklaas näitas külmakraade.
#Vastavate temperatuuride puudumisel, väljasta sobiv teade.
fail_sisse = open("kt_2.txt", "r")
kuupäevad = list()
kraadid = list()
mitu = int(fail_sisse.readline())
Mitu_kp = 0
Mitu_külm = 0
Summa_külm = 0

for rida in range(mitu):
    rida = fail_sisse.readline()
    abi = rida.split()
    kuupäevad.append(abi[0])
    kraadid.append(int(abi[1]))
fail_sisse.close()
    
for i in range(mitu):
    if kraadid[i] < 0:
        Summa_külm = Summa_külm + kraadid[i]
        Mitu_külm = Mitu_külm + 1

        

if Summa_külm != 0:
    Keskmine_külm = Keskmine_külm = Summa_külm / Mitu_külm
    print("Selle kuu külmakraadide keskmine temperatuur oli", round(Keskmine_külm, 2))
else:
    print("Selles kuus polnud ühtegi külmakraadi.")