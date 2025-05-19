def totale_incassi(tupla):
    tot=0
    for prodotto in tupla:
            tot+=prodotto[1]*prodotto[2]
    return tot

def media_prezzo_prodotto(tupla_vendite, pro):
     media=0
     num=0
     for prodotto in tupla_vendite:
        if(prodotto[0]==pro):
              media+=prodotto[1]
              num+=1
     return media/num
def vendita_con_maggiore_importo(tupla_vendite):
    massimo=0
    
    for prodotto in tupla_vendite:
        if(prodotto[1]>massimo):
                massimo=prodotto[1]
                disp=prodotto[0]
    return  disp, massimo

tupla_vendite = (
("Telefono", 500, 3, "2023-10-01"), 
("Computer", 1200, 2, "2023-10-02"),
("Monitor", 300, 5, "2023-10-03"),
("Cuffie", 80, 10, "2023-10-04"),
("Smartwatch", 200, 7, "2023-10-05"),
("Tablet", 400, 4, "2023-10-06"),
("Laptop", 500, 3, "2023-10-01"),
("Telefono",1400,4,"2023-10-02")
)
while True:
    opzione=int(input("inserire 1 se si vuole vedere il totale delle vendite.\nInserire 2 se si vuole vedere il prezzo unitario di un prodotto.\ninserire 3 se si vuole vedere il prodotto con il maggiore importo.\nInserire 4 se si vuole uscire "))
    if(opzione<0 or opzione>3):
        print("opzione inserita sbagliata")
    elif(opzione==1):   
        print(totale_incassi(tupla_vendite))
    elif(opzione==2):
        print("inserire il nome del prodotto di cui si vuole vedere il prezzo unitario: ")
        pro=input()
        print(media_prezzo_prodotto(tupla_vendite, pro))
    
    elif(opzione==4):
        break
    else:
        print("il prodotto con il prezzo maggiore è: ",vendita_con_maggiore_importo(tupla_vendite))


