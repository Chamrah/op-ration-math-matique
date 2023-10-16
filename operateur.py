#Programme qui fait une operation mathematique sur deux nombres entier
n1=int(input("Entrer un nombre entier : "))
n2=int(input("Entrer un deuxieme nombre entier : "))
o=input("Veuillez entrer l'operateur : ")
if(o=="+"):
    r=n1+n2
    print(f"Le resultat est : {r}")
elif(o=="-"):
    r=n1-n2
    print(f"Le resultat est : {r}")
elif(o=="x"):
    r=n1*n2
    print(f"Le resultat est : {r}")
elif(o=="/"):
    r=n1/n2
    print(f"Le resultat est : {r}")
else:
    print("Error")
