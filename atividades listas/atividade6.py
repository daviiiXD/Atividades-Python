notasAlunos = [0, 0, 0, 0]

notaAluno1 = ["nota1", "nota2", "nota3", "nota4"]
notaAluno2 = ["nota1", "nota2", "nota3", "nota4"]
notaAluno3 = ["nota1", "nota2", "nota3", "nota4"]
notaAluno4 = ["nota1", "nota2", "nota3", "nota4"]

notaAluno1[0] = int(input("Digite a sua primeira nota: "))
notaAluno1[1] = int(input("Digite a sua segunda nota: "))
notaAluno1[2] = int(input("Digite a sua terceira nota: "))
notaAluno1[3] = int(input("Digite a sua quarta nota: "))

notaAluno2[0] = int(input("Digite a sua primeira nota: "))
notaAluno2[1] = int(input("Digite a sua segunda nota: "))
notaAluno2[2] = int(input("Digite a sua terceira nota: "))
notaAluno2[3] = int(input("Digite a sua quarta nota: "))

notaAluno3[0] = int(input("Digite a sua primeira nota: "))
notaAluno3[1] = int(input("Digite a sua segunda nota: "))
notaAluno3[2] = int(input("Digite a sua terceira nota: "))
notaAluno3[3] = int(input("Digite a sua quarta nota: "))

notaAluno4[0] = int(input("Digite a sua primeira nota: "))
notaAluno4[1] = int(input("Digite a sua segunda nota: "))
notaAluno4[2] = int(input("Digite a sua terceira nota: "))
notaAluno4[3] = int(input("Digite a sua quarta nota: "))

somaAluno1 = notaAluno1[0] + notaAluno1[1] + notaAluno1[2] + notaAluno1[3]
somaAluno2 = notaAluno2[0] + notaAluno2[1] + notaAluno2[2] + notaAluno2[3]
somaAluno3 = notaAluno3[0] + notaAluno3[1] + notaAluno3[2] + notaAluno3[3]
somaAluno4 = notaAluno4[0] + notaAluno4[1] + notaAluno4[2] + notaAluno4[3]

notasAlunos[0] = somaAluno1 / 4
notasAlunos[1] = somaAluno2 / 4
notasAlunos[2] = somaAluno3 / 4
notasAlunos[3] = somaAluno4 / 4

passaram = 0

for i in notasAlunos :
    if i > 7 :
        print("Passou")
        passaram = passaram + 1

print(passaram)