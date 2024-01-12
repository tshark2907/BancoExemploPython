from datetime import datetime
dataEHora = datetime.now()
formatoPersonalizado = '%d/%m/%Y %H:%M:%S'
dataEHoraFormatada = dataEHora.strftime(formatoPersonalizado)
usuarios = {}
usuarioLogado = []
idConta = 1

def start():
    comando = input(
        'Seja bem-vindo ao Banco Exemplo!\n'+
        'Selecione uma das opções para prosseguir:\n\n'+
        '[1] Criar um novo usuário\n'+
        '[2] Entrar em um usuário existente\n\n')

    if comando == '1':
        criarUsuario()
    elif comando == '2':
        logarEmConta()

def avaliarCredito(usuario):
    balanco = 0
    if(usuario[0]['contas']):
        for conta in usuario[0]['contas']:
            if(conta['tipo'] == 'PJ'):
                balanco += float(conta['saldo']) + 500
                creditoAprovado = balanco * 2.5
                conta['limite_credito'] = creditoAprovado
                print('\nSeu crédito foi reavaliado! Limite atualizado: '+str(conta['limite_credito'])+' R$.')
                menuPrincipal()
            else:      
                balanco += float(conta['saldo'])
                if(balanco > 1500):
                    creditoAprovado = balanco * 1.3        
                    conta['limite_credito'] += creditoAprovado
                    print('\nSeu crédito foi reavaliado! Limite atualizado: '+str(conta['limite_credito'])+' R$.')
                    menuPrincipal()
                elif(balanco >= 500):
                    creditoAprovado = balanco * 0.5
                    conta['limite_credito'] = creditoAprovado
                    print('\nSeu crédito foi reavaliado! Limite atualizado: '+str(conta['limite_credito'])+' R$.')
                    menuPrincipal()
                else:
                    print('\nLamentamos, a funcionalidade de crédito ainda não está disponível para seu usuário\n'+
                    'Tente movimentar sua conta para que a funcionalidade seja habilitada.\n')
                    menuPrincipal()

def criarUsuario():
    cpf = input('\nInsira seu CPF, por favor: \n\n')
    if cpf in usuarios:
        print("\nUsuário já existe! Iniciando sistema de login\n\n")
        logarEmConta()
        return

    usuario = {
        "name": input('\nInsira seu nome completo, por favor: \n\n'),
        "cpf": cpf,
        "endereco": input('\nAgora, insira seu endereço por favor: \n\n'),
        "cep": input('\nInsira seu CEP por favor: \n\n'),
        "telefone": input('\nInsira seu número de telefone, sem o "55 XX":\n\n'),
        "email": input('\nInsira seu endereço de email por favor: \n\n'),
        "senha": input('\nCrie uma senha de acesso ao sistema: \n\n'),
        "agencia": '0001',
        "dataDeAbertura": str(dataEHoraFormatada),
        "contas":[]
    }
    
    confirmation = input(
        '\nConfirme os dados abaixo e autorize para a criação da conta:\n\n'
        '- Nome: '+str([usuario["name"]])+'\n'+
        '- CPF: '+str([usuario["cpf"]])+'\n'+
        '- Endereço: '+str([usuario["endereco"]])+'\n'+
        '- CEP: '+str([usuario["cep"]])+'\n'+
        '- Telefone: '+str([usuario["telefone"]])+'\n'+
        '- Email: '+str([usuario["email"]])+'\n'+
        '\nVocê confirma os dados?\n\n'+
        '[1]Confirmo\n'+
        '[2]Preciso corrigir os dados\n')
    
    if confirmation == '1':
        usuarios[cpf] = usuario
        print('\nUsuário criado com sucesso\n')
        logarEmConta()
    else:
        criarUsuario()

def criarConta(usuario):
    nova_conta = dict()
    nova_conta["apelido"] = input('\nInsira um nome para sua conta:\n')
    nova_conta["tipo"] = input('\nSua conta será empresarial ou pessoal?\n[1] Pessoa Física\n[2] Pessoa Jurídica\n')
    nova_conta['limite_credito'] = 0.00
    nova_conta['saldo'] = 0.00
    if(nova_conta['tipo'] == '1'):
        nova_conta['tipo'] = 'PF'
    elif(nova_conta['tipo'] == '2'):
        nova_conta['tipo'] = 'PJ'
    
    querCredito = input('\nDeseja solicitar a funcionalidade de crédito em sua conta?\n[1] Sim\n[2] Não\n\n')
    if querCredito == '1':
        balanco = 0
        for conta in usuario['contas']:
            if conta['tipo'] == 'PJ':
                balanco += float(conta['saldo']) + 500
                creditoAprovado = balanco * 2.5
                nova_conta['limite_credito'] = creditoAprovado
            else:
                balanco += float(conta['saldo'])
                if balanco > 1500:
                    creditoAprovado = balanco * 1.3        
                    nova_conta['limite_credito'] = creditoAprovado
                elif balanco >= 500:
                    creditoAprovado = balanco * 0.5
                    nova_conta['limite_credito'] = creditoAprovado
                else:
                    print('\nLamentamos, a funcionalidade de crédito ainda não está disponível para seu usuário\n'+
                          'Tente movimentar sua conta para que a funcionalidade seja habilitada.\n')
                    menuPrincipal()

    global idConta
    nova_conta['id'] = idConta
    idConta += 1
    confirmation = input(
        '\nConfirme os dados abaixo para criar sua conta:\n\n'+
        'Nome da conta: '+nova_conta['apelido']+'\n'+
        'Tipo de conta: '+nova_conta['tipo']+'\n'+
        '\nOs dados estão corretos?\n[1] Sim, criar minha conta.\n[2] Não, cancelar.\n')
    
    if confirmation == '1':
        print('Carregando...')
        cpf_usuario = usuario["cpf"]
        if cpf_usuario in usuarios:
            usuarios[cpf_usuario]['contas'].append(nova_conta)
            print('\nAdicionando a conta '+nova_conta['apelido']+'.\n')
            menuPrincipal()
    elif confirmation == '2':
        criarConta(usuario)
 
def logarEmConta():
    cpf = input('Insira seu CPF para acessar sua conta:\n')
    senha = input('Insira sua senha de acesso:\n')

    if cpf in usuarios:
        usuario = usuarios[cpf]
        if senha == usuario['senha']:
            usuarioLogado.append(usuario)
            print('\nSeja bem-vindo ' + str(usuario['name'].split(' ')[0]) + '!\n')
            if(len(usuario['contas']) > 0):
                menuPrincipal()
            else:
                criarConta(usuarioLogado[0])
        else:
            print('\nSenha incorreta, tente novamente.\n')
            start()
    else:
        print('\nUsuário não encontrado, verifique o CPF e tente novamente.\n')
        start()


def extrato(usuario):
    for conta in usuario[0]['contas']:
        print(
            '\n\nNome da conta: '+conta['apelido']+'\n'+
            'Tipo de conta: '+conta['tipo']+'\n'+
            'Saldo atual: '+str(conta['saldo'])+' R$\n'+
            'Crédito disponível: '+str(conta['limite_credito'])+' R$\n'+
            '\n\n')
    menuPrincipal()
    
def credito(usuario):
    for conta in usuario[0]['contas']:
        print(
            '\n\nNome da conta: '+conta['apelido']+'\n'+
            'Tipo de conta: '+conta['tipo']+'\n'+
            'Crédito disponível: '+str(conta['limite_credito'])+' R$\n'+
            '\n\n')
    menuPrincipal()
    
def deposito(usuario):
    quantia = input('\nDigite a quantidade a ser depositada:\n')
    counter = 1
    for conta in usuario[0]['contas']:
        print('\n['+str(counter)+']''Conta : '+conta['apelido']+'| Saldo: '+str(conta['saldo'])+' R&.\n')
    comand = input('\nEm qual conta deseja depositar?\n')
    if(usuario[0]['contas'][int(comand) - 1]):
        confirmarSenha = input('\nInsira sua senha para prosseguir:\n')
        if(confirmarSenha == usuario[0]['senha']):
            usuario[0]['contas'][int(comand) - 1]['saldo'] += float(quantia)
            print('\nSaldo atualizado: '+ str(usuario[0]['contas'][int(comand) - 1]['saldo'])+' R$\n')
            menuPrincipal()
        else:
            print('\nSenha incorreta, tente novamente\n')
            menuPrincipal()
    else:
        print('\nConta não encontrada, tente novamente.\n')
        menuPrincipal()
        
def saque(usuario):
    quantia = input('\nDigite a quantidade a ser sacada:\n')
    counter = 1
    for conta in usuario[0]['contas']:
        print('\n['+str(counter)+']''Conta : '+conta['apelido']+'Saldo: '+str(conta['saldo'])+' R&.\n')
    comand = input('\nDe qual conta deseja sacar?\n')
    if(usuario[0]['contas'][int(comand) - 1]):
        if(float(usuario[0]['contas'][int(comand) - 1]['saldo']) >= float(quantia)):
            usuario[0]['contas'][int(comand) - 1]['saldo'] -= float(quantia)
            confirmarSenha = input('\nInsira sua senha para prosseguir:\n')
            if(confirmarSenha == usuario[0]['senha']):
                print('\nSaldo atualizado: '+ str(usuario[0]['contas'][int(comand) - 1]['saldo'])+' R$\n')
                menuPrincipal()
            else:
                print('\nSenha incorreta, tente novamente\n')
                menuPrincipal()
        else:
            print('\nSaldo insuficiente, tente novamente.\n')
            menuPrincipal()
    else:
        print('\nConta não encontrada, tente novamente.\n')
        menuPrincipal()
        
def transferencia(usuario):
    counter = 1
    for conta in usuario[0]['contas']:
        print('\n['+str(counter)+']''Conta : '+conta['apelido']+'Saldo: '+str(conta['saldo'])+' R&.\n')
    origin = input('\nDe qual conta deseja transferir?\n')
    quantia = input('\nDigite a quantidade a ser sacada:\n')
    destino = input('\nInsira o CPF do usuário que deverá receber a transferência\n\n')
    global usuarios
    if destino in usuarios:
        target = usuarios[destino]
        print('Usuario localizado')
        if(len(target['contas']) > 0):
            counterAlheio = 1
            print('\nExibindo contas de '+target['name']+'.\n')
            for contaAlheia in target['contas']:
                print('\n['+str(counterAlheio)+'] '+target['name'] +' - '+contaAlheia['apelido'])
            confirmation = input('Para qual conta você deseja transferir a quantia de '+str(quantia)+' R$?\n')
            if(target['contas'][int(confirmation) - 1]):
                confirmarSenha = input('\nInsira sua senha para prosseguir:\n')
                if(confirmarSenha == usuario[0]['senha']):
                    target['contas'][int(confirmation) - 1]['saldo'] += float(quantia)
                    print(
                        '\nTransferência concluida com sucesso\n\n'+
                        'De: '+usuario[0]['contas'][int(origin) - 1]['apelido']+'\n'+
                        'Para: '+target['name']+' | '+target['contas'][int(confirmation) - 1]['apelido']+'\n'+
                        'Valor: '+str(quantia)+' R$\n'+
                        'Data: '+dataEHoraFormatada+' \n')
                    menuPrincipal()
                else:
                    print('\nSenha incorreta, transação cancelada.\n')
                    menuPrincipal()
            else:
                print('\nConta inexistente, transação cancelada.\n')
                menuPrincipal()
        else:
            print('\nUsuário inexistente, operação cancelada.\n')
            menuPrincipal()
            
def logout(usuario):
    usuario.clear()
    start()
    
def sobre(usuario):
    print('\nExibindo informações de '+usuario[0]['name'].split(' ')[0]+'.\n'+
          'Cliente desde: '+usuario[0]['dataDeAbertura']+'.\n\n')
    comand = input('Voce deseja encerrar sua conta?\n[1] Não.\n[2] Sim.\n')
    if(comand == '1'):
        menuPrincipal()
    elif(comand == '2'):
        confirmarSenha = input('Insira sua senha para prosseguir:\n')
        if(confirmarSenha == usuario[0]['senha']):
            for element in usuarios:
                if(element['cpf'] == usuario[0]['cpf']):
                    usuarios.discard(element)
                    usuario.clear()
                    print('Conta deletada com sucesso, foi um prazer te ter como cliente!\n')
                    start()
        else:
            print('Senha incorreta. Tente novamente')
            menuPrincipal()
    else:
        print('Comando inválido. Tente novamente.\n')
        menuPrincipal()
                            
def menuPrincipal():
    comando = input(
        'O que deseja fazer '+str(usuarioLogado[0]['name'].split(' ')[0])+'?\n\n'+
        '[1] Obter o extrato da(s) conta(s):\n'
        '[2] Depositar dinheiro:\n'+
        '[3] Sacar dinheiro:\n'+
        '[4] Transferir dinheiro:\n'+
        '[5] Verificar situação de crédito:\n'+
        '[6] Criar uma nova conta no Banco Exemplo:\n'+
        '[7] Sobre seu usuário no Banco Exemplo:\n'+
        '[8] Requisitar crédito para minha conta:\n' 
        '[9] Sair da conta:\n\n')
    if(comando == '1'):
        extrato(usuarioLogado)
    elif(comando == '2'):
        deposito(usuarioLogado)
    elif(comando == '3'):
        saque(usuarioLogado)
    elif(comando == '4'):
        transferencia(usuarioLogado)
    elif(comando == '5'):
        credito(usuarioLogado)
    elif(comando == '6'):
        criarConta(usuarioLogado[0])
    elif(comando == '7'):
        sobre(usuarioLogado)
    elif(comando == '8'):
        avaliarCredito(usuarioLogado)
    elif(comando == '9'):
        logout(usuarioLogado)
    else:
        print('Opção inválida!')
        menuPrincipal()
        
start()