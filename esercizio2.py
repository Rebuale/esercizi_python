def analizza_utilizzo_servizi(tupla_utilizzo_servizi,città, servizio):
    media_servizio=media_utilizzo_servizio(tupla_utilizzo_servizi, città, servizio)
    mese_max_servizio,max_servizio=massimo_utilizzo_servizio(tupla_utilizzo_servizi, città, servizio)
    return (media_servizio), (max_servizio, mese_max_servizio)


def media_utilizzo_servizio(tupla_utilizzo_servizi, città, servizio):
    media_servizio=0
    mesi=0
    for citta in tupla_utilizzo_servizi: 
       for servizi in citta:
           if(citta[0]==città):
               if(type(servizi)==tuple):
                   if(servizi[1][0]==servizio):
                       media_servizio+=servizi[1][1]
                       mesi+=1
    return media_servizio/mesi

def massimo_utilizzo_servizio(tupla_utilizzo_servizi, città, servizio):    
    max_servizio=0
    for citta in tupla_utilizzo_servizi: 
       for servizi in citta:
           mese=servizi[0]
           if(citta[0]==città):
               if(type(servizi)==tuple):
                   if(servizi[1][0]==servizio):
                       if(max_servizio<servizi[1][1]):
                           max_servizio=servizi[1][1]
                           mese_max=mese

    return mese_max, max_servizio
tupla_utilizzo_servizi = (
    ("Roma", 
        ("gennaio", ("trasporti_pubblici", 12000)), 
        ("gennaio", ("parcheggi", 8000)), 
        ("febbraio", ("trasporti_pubblici", 11000)),
        ("febbraio", ("parcheggi", 7500)),
        ("marzo", ("trasporti_pubblici", 12400)), 
        ("marzo", ("parcheggi", 8300)), 
        ("aprile", ("trasporti_pubblici", 10000)),
        ("aprile", ("parcheggi", 3500)),
 
    ),
    ("Napoli", 
        ("gennaio", ("trasporti_pubblici", 9000)),
        ("gennaio", ("parcheggi", 6000)),
        ("febbraio", ("trasporti_pubblici", 8500)),
        ("febbraio", ("parcheggi", 5500)),
        ("marzo", ("trasporti_pubblici", 12400)), 
        ("marzo", ("parcheggi", 8300)), 
        ("aprile", ("trasporti_pubblici", 10000)),
        ("aprile", ("parcheggi", 3500)),
     
    ))


città=input("inserire il nome della città che si vuole vedere: ")
servizio=input("inserire il tipo di servizio che si vuole analizzare: ")
analizza=analizza_utilizzo_servizi(tupla_utilizzo_servizi,città,servizio)
print(f"la media del servizio {servizio} è {analizza[0]}. il massimo registrato del servizio è di {analizza[1][0]} nel mese di{analizza[1][1]}")