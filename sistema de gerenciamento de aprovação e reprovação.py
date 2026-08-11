nome =input("qual é o seu nome ?")
nota =float(input("qual a sua nota ?"))
print(f" Olá,{nome}")
if nota == 10:
    print(" Parabéns, aprovado com louvor!")
elif nota >= 6:
    print(" Aprovado, na média")
else:
    print("reprovado")
    