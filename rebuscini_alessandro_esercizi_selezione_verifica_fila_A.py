#esercizio 1
v1=int(input("inserire 3 voti il trentesimi.\nPrimo voto: "))
v2=int(input("Seondo voto: "))
v3=int(input("Terzo voto: "))
if(v1> 30 or v2> 30 or v3 > 30):
    print("uno dei voti inseriti è maggiore di 30")
else:
    ct=int(input("Inserire 1 se si vuole la media in centesimi, inserire 2 se si vuole la media in trentesimi: "))
    m1=(v1+v2+v3)/3
    if(ct==1):
        m1=m1*100/30
        print("la media in centesimi è di: ",m1)
    elif(ct==2):
        print("la media in trentesimi è di: ",m1)
    else:
        print("Numero inserito sbagliato")


#esercizio 2 

m=float(input("Inserire la media dello studente: "))
a=int(input("Inserire l'anno scolastico di cui fa parte lo studente (3,4,5): "))
if(m<=10):
    if(a==3):
        if(m<6):
            print("i crediti assegnati sono 0")
        elif(m==6):
            print("i crediti assegnati sono 7-8")
        elif(m<=7):
            print("i crediti assegnati sono 8-9")
        elif(m<=8):
            print("i crediti assegati sono 9-10")
        elif(m<=9):
            print("i crediti assegati sono 10-11")
        elif(m<=10):
            print("i crediti assegati sono 11-12")
        
    elif(a==4):
        if(m<6):
            print("i crediti assegnati sono 0")
        elif(m==6):
            print("i crediti assegnati sono 8-9")
        elif(m<=7):
            print("i crediti assegnati sono 9-10")
        elif(m<=8):
            print("i crediti assegati sono 10-11")
        elif(m<=9):
            print("i crediti assegati sono 11-12")
        elif(m<=10):
            print("i crediti assegati sono 12-13")
    elif(a==5):
        if(m<6):
            print("i crediti assegnati sono 0")
        elif(m==6):
            print("i crediti assegnati sono 9-10")
        elif(m<=7):
            print("i crediti assegnati sono 10-11")
        elif(m<=8):
            print("i crediti assegati sono 11-12")
        elif(m<=9):
            print("i crediti assegati sono 13-14")
        elif(m<=10):
            print("i crediti assegati sono 14-15")
    else:
        print("anno inserito sbalgiato")
else:
    print("media inserita è superiore al 10")

#esercizio 3 

l1=float(input("inserire la lunghezza del primo lancio. Inserire 0 se è nullo: "))
l2=float(input("inserire la lunghezza del secondo lancio. Inserire 0 se è nullo: "))
l3=float(input("inserire la lunghezza del terzo lancio. Inserire 0 se è nullo: "))
l4=float(input("inserire la lunghezza del quarto lancio. Inserire 0 se è nullo: "))
l5=float(input("inserire la lunghezza del quinto lancio. Inserire 0 se è nullo: "))
c=5 #contatore lanci validi
if(l1==0 and l2==0  and l3==0 and l4==0 and l5==0):
    print("tutti i lanci sono nulli")
else:
    if(l1==0):
        c-=1
    if(l2==0):
        c-=1
    if(l3==0):
        c-=1
    if(l4==0):
        c-=1
    if(l5==0):
        c-=1
    m3=(l1+l2+l3+l4+l5)/c
    print("la media dei lanci validi è pari a: ",m3)