from pyfiglet import Figlet

def opcoesadmin():
    print("#>#"*30)
    print("#" * 5, " " * 78, "#" * 5)
    print("#"*5, "           1- Adcionar Tema ", " " * 49, "#"*5)
    print("#"*5, "           2- Adcionar Palavra/Frase ao Tema ", " " * 32, "#"*5)
    print("#" * 5, "           3- Remover Palavra/Frase do Tema ", " " * 33, "#" * 5)
    print("#" * 5, "           4- Remover  Tema ", " " * 49, "#" * 5)
    print("#" * 5, " " * 78, "#" * 5)
    print("#>#"*30)

def escolha():
    num = int(input("Digite sua Escolha: "))
    return num

def intro():
    fig = Figlet(font='clR6x8')
    print("#>#" * 15)
    print(" " * 30)
    print(" " * 30)
    print(f"{fig.renderText('ADMIN')}")
    print("#>#" * 15)


def menuadmin():
    intro()
    opcoesadmin()
    esc = escolha()
    # chamar classe de Controle
