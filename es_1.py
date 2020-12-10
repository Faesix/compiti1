parola = input("Qual è la parola? ")
parola_palindroma = parola[::-1]
if parola == parola_palindroma:
    print(parola, "è palindroma")
else:
    print(parola + "non è palindroma")
