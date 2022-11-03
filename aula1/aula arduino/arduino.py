notas = []
def media() :
    media = 0
    for i in range(1 , 5) :
        notas.append(int(input(f"Digite sua {i}° nota: ")))
    media = (notas[0] + notas[1] + notas[2] + notas[3]) / len(notas)
    if media > 6 :
        print("True 😎")
    else :
        print("False 😭")
    print(media)

media()python3 main.py