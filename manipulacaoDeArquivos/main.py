try:
    with open("manipulacaoDeArquivos/arquivos/teste.txt", "r") as arquivo :
        print(arquivo.read)
except FileNotFoundError:
    print("Arquivo não encontrado")

try: 
    with open("manipulacaoDeArquivos/arquivos/arquivo.md", 'w') as arquivo :
        arquivo.write("Olá munfgsgfsdo")
except FileNotFoundError:
    print("Não foi possivel gravar em arquivos")