class Fuvar:
    def __init__(self,id,ido,idotartam,tavolsag,dij,borravalo,fmod):
        self.id=id
        self.ido=ido
        self.idotartam=idotartam
        self.tavolsag=tavolsag
        self.dij=dij
        self.borravalo=borravalo
        self.fmod=fmod
        

f = open("fuvar.csv", "rt", encoding="utf-8")

f.readline()

adatok = []

for sor in f:
    sor = sor.strip().split(";")

    adatok.append(Fuvar(sor[0],sor[1],sor[2],sor[3],float(sor[4].replace(",",".")),float(sor[5].replace(",",".")),sor[6],))

print(f"3. feladat: {len(adatok)-1} fuvar")


bevetel = 0
fuvarszam = 0

for fuvarok in adatok:
    if fuvarok.id == "6185":
        bevetel += fuvarok.dij + fuvarok.borravalo
        fuvarszam += 1
bevetel = str(bevetel)
print(f"{fuvarszam} fuvar alatt {bevetel.replace(".",",")}$")
        