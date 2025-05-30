import os #biblioteca utilizada para interagir com o sistema operacional subjacente, permitindo que o código manipule arquivos, diretorios, processos, variáveis de ambiente e obtenha informações sobre o sistema.

restaurantes = ['Pizza', 'Sushi', 'Salgado', 'Churrasco'] #lista de todos os restaurantes que serão cadastrados.

def exibirNomePrograma(): #Função responsável por exibir o nome do programa
    print('Sabor express\n ')

def exibeOpcao(): #Função responsável por mostrar o menu de opções do sistema
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Ativar restaurante')
    print('4 - Sair')

def finalizar_app():#Função que irá limpar a tela e informar que o sistema está sendo finalizado.
    exibir_substitulo('Finalizando o programa')

def voltar_ao_menu_principal():#Função criada para facilitar a manutenção da parte de voltar ao menu principal.
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida(): #função criada para quando o usuário digitar uma opção inválida (string ou numero que não faça parte do menu) e executar o main novamente.
    print('Opção inválida\n ')
    voltar_ao_menu_principal()

def exibir_substitulo(texto): #Criado para facilitar no entendimento do código, utilizando apenas uma função para  que possamos atualizar muitas informações.
    os.system('cls')
    print(texto)

def cadastra_restaurante(): #função criada para cadastrar os restaurantes, onde informamos o nome do mesmo e adicionamos a lista 'restaurantes', logo após podemos digitar qualquer tecla e voltar ao  inicio do sistema.
    exibir_substitulo('Cadastro de novos restaurantes')
    nomeRestaurante = input('Informe o nome do restaurante que a ser cadastrado: ')
    restaurantes.append(nomeRestaurante)#Adicionar informação a lista
    print(f'O restaurante {nomeRestaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def lista_restaurante(): #função responsável por mostrar os restaurantes cadastrados no nosso sistema.
    exibir_substitulo('Listando todos os restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu_principal()

def escolheOpcao():#Função que irá mostrar a opção que voce escolheu

    try: #Está pedindo para tentar uma das opções do sistema, caso não consiga nenhuma ele irá ativar a condição except.
        op = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {op}')

        if op == 1:
            cadastra_restaurante()
        elif op == 2:
            lista_restaurante()
        elif op == 3:
            print('Ativar restaurante')
        elif op == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: #ativa a função que nos manda digitarmos uma tecla e voltar ao menu principal.
        opcao_invalida()

def main():#Função que executa todas as outras funções do programa.
    os.system('cls')
    exibirNomePrograma()
    exibeOpcao()
    escolheOpcao()

if __name__ == '__main__':#Informando que este código é o main, não poderá ser importado por outros scripts de código python, ele é o programa principal.
    main()

