def funcaoLogin() :
    print('Cadastro 😶')
    nome = input('Seu Nome: ')
    idade = int(input('Sua idade: '))
    # - Verifica se o usuario é maior de idade :)
    if idade < 18 :
        print('- Você não tem idade suficiente para entrar 😔')
        funcaoLogin()
    else :
        print('- Acesso concedido 😏')
        login = input('Seu Login: ')
        senha = input('Sua Senha: ')
        confirmarSenha = input('Confirme sua senha: ')
        tamanhoSenha = len(senha)
        # verifica a confirmação da senha e o seu tamanho
        if confirmarSenha == senha and tamanhoSenha > 5 :
            print('Parabéns ' + login + ' sua conta foi criada com sucesso 🤑')
            print('Nome: ' + nome)
            print('Login: ' + login)
            print('idade: ' + str(idade))
            print('Senha: ' + senha)
        else :
            print('As senhas não batem ou elas são muito pequenas 😂 tente novamente 😀')
            funcaoLogin()
funcaoLogin()