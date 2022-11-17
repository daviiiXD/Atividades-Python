contador = 0
def exibirMenu():
     with open("vendaDeLivros/assets/menu.txt", 'r') as file:
          print(file.read())

def cadastrarLivro():
     global contador
     with open('vendaDeLivros/assets/livros.txt', 'a+') as file:
          file.write(f'{input("Digite o nome do autor: ")}, {input("Digite o nome do livro: ")}, {contador} \n')
          contador += 1
          file.close()

def exibirLivros():
     print('Você cadastrou os seguintes livros: ')
     for i in livros:
          print(i)

def buscarLivro():
     livroBusca = input("Digite o nome do livro: ")
     print('O livro que você pesquisou é: ')
     print(livros[livroBusca])


while(True):
     exibirMenu()
     try:
          opcao = int(input("Digite a opção por favor "))
          if opcao == 1:
               cadastrarLivro()
          elif opcao == 2:
               exibirLivros()
          elif opcao == 3:
               buscarLivro()
          elif opcao == 4:
               break
     except ValueError:
          print("Você não digitou um número. ")