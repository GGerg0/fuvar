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

adatok = []

for sor in f:
    sor = sor.strip().split(";")
    adatok.append(Fuvar(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5],sor[6],))

    