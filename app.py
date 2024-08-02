import os

def exibir_nome():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      ''') 
    
def menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando')

def escolher_opcoes():           
    opcao_escolhida = int(input('escolha uma opção:'))

    if opcao_escolhida == 1:
        print('1. Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('2. Listar restaurante')
    elif opcao_escolhida == 3:
        print('3. Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome()
    menu()
    escolher_opcoes()

if __name__ == '__main__':
    main()