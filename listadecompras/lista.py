lista = []
def adicionar(item) :
    lista.append(item)
def removerUltimo() :
    lista.pop()
def removerPorIndice(item) :
    lista.pop(item)
def removerPorValor(item) :
    lista.remove(item)
def limpar() :
    lista.clear()
def sair() :
    print("Obrigado por usar o meu programa 😀")
def menu() :
    print("-----------------------------------------")
    if len(lista) == 0 :
        print("Sua lista está vazia BB 😁")
    if len(lista) > 0 :
        print("Sua lista está assim :")
    for i in lista :
        print(i)
    print("-----------------------------------------")
    print("-----------------------------------------")
    print("1 - Inserir um item na lista")
    print("2 - Remover o ultimo item da lista")
    print("3 - Remover um item da lista pelo indice")
    print("4 - Remover um item pelo valor")
    print("5 - Limpar tudo")
    print("6 - Sair")
    print("-----------------------------------------")
def pedir() :
    opcao = input("Digite a opção desejada: ")
    if opcao == "1" :
        adicionar(input("Digite um item para adicionar a lista: "))
        menu()
        pedir()
    elif opcao == "2" :
        removerUltimo()
        menu()
        pedir()
    elif opcao == "3" :
        removerPorIndice(int(input("Digite o indice do item: ")))
        menu()
        pedir()
    elif opcao == "4" :
        removerPorValor(input("Digite o nome do item: "))
        menu()
        pedir()
    elif opcao == "5" :
        limpar()
        print(lista)
        menu()
        pedir()
    elif opcao == "6" :
        sair()
def iniciar() :
    contador = 0
    while True :
        contador = contador + 1
        pergunta = input(f"Digite o nome do {i} item da lista ou [m] para exibir o menu: ")
        if pergunta ==  "m" :
            menu()
            pedir()
            break
        else :
            lista.append(pergunta)
            print(f"{pergunta} adicionado")
            for i in lista :
                print(i)
iniciar()