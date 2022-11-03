notas = ["nota1", "nota2", "nota3", "nota4"]

notas[0] = int(input("Digite a sua primeira nota: "))
notas[1] = int(input("Digite a sua segunda nota: "))
notas[2] = int(input("Digite a sua terceira nota: "))
notas[3] = int(input("Digite a sua quarta nota: "))

soma = notas[0] + notas[1] + notas[2] + notas[3]

media = soma / 4

print("Sua media é: " + str(media))