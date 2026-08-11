nome =input("qual é o seu nome ?")
nota =float(input("qual é a sua nota ?"))
print(f"Olá, {nome}")
if nota > 10:
    print("Valor inválido, tente novamente")
elif nota == 10:
    print("Parabéns, aprovado com nota máxima")
elif 8 < nota <= 9.9:
    print("aprovado com nota excelente,parabéns")
elif 6.9 <= nota <= 7.9:
    print("aprovado com uma boa nota, parabéns")
elif nota == 6:
    print("aprovado na média, parabéns")
elif 0 < nota < 6:
    print("reprovado, sinto muito")
elif nota < 0:
    print(" Valor inválido, tente novamente")


    