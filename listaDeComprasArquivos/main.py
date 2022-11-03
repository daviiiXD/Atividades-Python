lista = []
opcao = 0
def criarLinha(titulo, quantidade) :
     print('-' * quantidade, titulo, '-' * quantidade)

def escreverNoArquivo(nome) :
     try: 
          with open("listaDeComprasArquivos/database.txt", 'w+') as arquivo :
               for i in lista :
                    arquivo.write(i + '\n')
     except FileNotFoundError:
          print("Não foi possivel gravar em arquivos")
while True :
     criarLinha('Lista de compras', 30)
     print("1 - Inserir um item na lista")
     print("2 - Sair")

     opcao = int(input('Escolha uma opção: '))

     if opcao == 1 :
          lista.append(input("Digite o nome do item: "))
          for i in lista :
               escreverNoArquivo(i)
