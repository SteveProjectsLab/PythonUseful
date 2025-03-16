print("##############################################")
print("\tcalcolatore tolleranze componenti\n\tStefano Molari")
print("##############################################\n")
scelta=0
continua=1
while(1):
    comp=0
    scelta=input("seleziona il tipo di componente:\
                 \n\"1\"- 1%\
                 \n\"2\"- 5%\
                 \n\"3\"- 10%\
                 \n\"4\"- 20%\
                 \n\"5\"- esci\n")

    if(scelta =="1"):
        comp=input("inserisci valore:")
        tol=1
    elif(scelta =="2"):
        comp=input("inserisci valore:")
        tol=5
    elif(scelta =="3"):
        comp=input("inserisci valore:")
        tol=10
    elif(scelta =="4"):
        comp=input("inserisci valore:")
        tol=20
    elif(scelta =="5"):
        print("----------------------------------------------------")
        print("chiusura programma..")
        print("----------------------------------------------------")
        exit()
    else:
        print("\nhai sbagliato a inserire..\n")
    compinf=float(comp)*(1-tol/100)
    compsup=float(comp)*(1+tol/100)
    print("----------------------------------------------------")
    print("min:"+str(float(compinf))+"\nmax:"+str(float(compsup)))
    print("----------------------------------------------------") 
    comp=input("se vuoi continuare premi y:")
    if(comp=="y"or comp=="Y"):
        continua=1
    else:
        exit()
