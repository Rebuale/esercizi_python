negozi=["lidl", "iper", "eurospin"]
vendite_max=[]
vendite_min=[]
vmaxtot=0
vmintot=0
for i in range(len(negozi)):
    print("inserire la vendita massima del",negozi[i])
    v=int(input())
    vendite_max.append(v)
    vmaxtot+=v
    print("inserire la vendita minima del",negozi[i])
    v=int(input())
    vendite_min.append(v)
    vmintot+=v
vmmax=vmaxtot/len(vendite_max)
print(f"la media delle vendite massime registrate è {vmmax}")
vmmin=vmintot/len(vendite_min)
print(f"la media delle vendite minime registrate è di {vmmin}")
for i in range(len(negozi)):
    if(vmmin>vendite_min[i]):
        print(f"il negozio {negozi[i]} ha avuto una minima vendita inferiore a quella media")
if(negozi.__contains__(input("inserire il nome di un negozio: "))==True):
    print("il negozio inserito è presente nella lista")
else:
    print("il negozio non è presente nella lista")
