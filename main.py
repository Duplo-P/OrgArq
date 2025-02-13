from modulo import*

def menu():
    print('''
    1 - Organizar arquivos 
    2 - Ajuda
    3 - Sair
    '''.center(size()))
    opcao = input('Digite a opção desejada: ')
    return opcao
def size():
    largura, _ = os.get_terminal_size()
    return largura

if __name__ == '__main__':
    
    while True:
        os.system("clear")
        print('ORGANIZADOR DE ARQUIVOS'.center(size()))
        opcao = menu()
        if opcao == "1":
            organizar_arquivos()
        elif opcao == "2":
            print('''
            Organizar arquivos é um programa que organiza arquivos em pastas de acordo com a extensão do arquivo.
            ''')
        elif opcao == "3":
            break
        else:
            print('Opção inválida!')




    