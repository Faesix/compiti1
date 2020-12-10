A = []
B = []

while True:
    parola = input("Qual è la parola?, inserisci 0 per finire ")
    if parola == "0":
        break
    else:
        A.append(parola)
        B.append(len(parola))

print("Queste sono le parole: ", A)
print("Queste sono le loro lunghezze: ", B)
