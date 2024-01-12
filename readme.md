Projeto: Agência Bancária

Requisitos funcionais: 
            Possuir um sistema de criação de contas
            Possuir um sistema de saques e depósitos
            Possuir um sistema emissor de extratos
            Possuir um sistema de criação de usuários
            Deve possuir modularidade
            Usuário deve conseguir transferir dinheiro de uma conta para outra
            Usuário deve ser capaz de deletar contas e seu próprio usuário

Requisitos não funcionais:
            Sem limites de saque por conta
            Somente um usuario por cpf
            Sem limite no numero de contas criadas por usuário
            Cada funcionalidade deve ter sua função própria
            Se o balanço total do usuário for menor do que 500R$, 
            não será liberado crédito 

    Formato de criação de usuário:
        Nome:
        CPF:
        Endereço:
        Cep:
        Telefone:
        E-mail:
        Contas:

    Formato de criação de contas:
        Apelido da conta:
        Tipo de conta:[PF],[PJ]
        Deseja crédito:[Sim],[Não]
        Crédito disponível:(Calculado com base no balanço total
        do usuário, multiplicando por 1.3)

    