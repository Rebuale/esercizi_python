destinazioni = ["Roma", "Milano", "Parigi", "Praga", "Berlino"]
oreP = [10, 11,13,15,17]
oreA = [11,14,18,19,20]
d=input("inserisci la destinazione desiderata: ")
if(destinazioni.__contains__(d)):
    print("L'orario di partenza del volo per",d,"è",oreP[destinazioni.index(d)])
else:
    print("la destinazione non è registrata")
intervalloP=int(input("inserie l'intervallo di tempo in cui si vuole partire: "))
intervalloA=int(input())
for i in range(len(destinazioni)):
    if(oreP[i]>=intervalloP and oreA[i]<=intervalloA):
        print("il volo che parte nell'intervallo di tempo",intervalloP,intervalloA," è ",destinazioni[i],"che parte alle",oreP[i],"e dura",(oreA[i]-oreP[i]))
d=input("inserisci la destinazione desiderata: ")
if(destinazioni.__contains__(d)):
    om=oreA[destinazioni.index(d)]-oreP[destinazioni.index(d)]
    imin=destinazioni.index(d)
    for i in range(len(destinazioni)):
        if(destinazioni[i]==d and om>oreA[destinazioni.index(d)]-oreP[destinazioni.index(d)]):
            om=oreA[destinazioni.index(d)]-oreP[destinazioni.index(d)]
            imin=i
    print("il volo più veloce per",d,"è quello che parte a",oreP[imin],"e dura",om,"ore")
else:
    print("la destinazione inserita non è presente nei voli")
