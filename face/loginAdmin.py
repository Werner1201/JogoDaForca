from controle.verificaCredencial import *


def primeiratela():
    print("#" * 30)
    print("####### Login de Admin #######")
    print("#" * 30)
    print(" " * 30)
    nome = input("Login:")
    senha = input("Senha:")
    return controleLogin(nome, senha)


def error(numerr):
    erros = numerr
    print("Login ou Senha Inválidos")
    print(f"Digite novamente ({erros}/3)")
    nome = input("Login:")
    senha = input("Senha:")
    return controleLogin(nome, senha)


def containercontrole():
    if primeiratela():
        return True
        # executa o menu de Admin
    else:
        i = 1
        res = error(i)
        while not res or i > 3:
            i += 1
            res = error(i)
        if i > 3:
            print("Número de Tentativas Esgotada. Fechando o Programa.")

        # executa o menu pois funcionou
