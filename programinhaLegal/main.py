"""
Programa cadastro de Aluno.
Cadastra o nome e a média do aluno e salva em um dicionário
"""

aluno_media = {}
QTDA_CARACTERES = 60

def criar_linha(caracter, qtda):
    print(caracter * qtda)

def exibir_menu():
    criar_linha('*', QTDA_CARACTERES)
    print("MENU".center(QTDA_CARACTERES))
    criar_linha('*', QTDA_CARACTERES)

    print("""
        1 - CADASTRAR ALUNO  
        2 - MOSTRAR DADOS DO ALUNO     
        3 - SAIR
    """)
    criar_linha('*', QTDA_CARACTERES)

def mostrar_dados():
    if len(aluno_media) > 0:
        print("-" * QTDA_CARACTERES)
        print(f"\033[0;1;33mALUNOS CADASTRADOS = {len(aluno_media)}\033[m")
        print("-" * QTDA_CARACTERES)
        for k, v in aluno_media.items():
            print(f"\033[0;1;33m {k} => {v}\033[m")
            print("-" * QTDA_CARACTERES)
            print()
    else:
        print("\033[0;1;33mNão existe aluno cadastrado!\033[m")
        print()

def inserir_dados():
    nome = input("Digite o nome do aluno\n")
    media = float(input("Digite a média do aluno\n"))

    try :
        with open('programinhaLegal/database/alunos.py', 'w') as arquivo :
            aluno_media[nome] = media
            arquivo.write(str(aluno_media))
    except FileNotFoundError :
        print("Deu ruim")

while True:
    exibir_menu()
    opcao = int(input("Digite a opcao do menu.txt, por favor.\n"))
    if opcao == 1:
        inserir_dados()
    elif opcao == 2:
        mostrar_dados()
    elif opcao == 3:
        break