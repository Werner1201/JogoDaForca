from modelo.bancoPalavra import bancopalavra

class controlerodada:
    def __init__(self, situacaopalavra):
        self.letraserrada = ""
        self.situacaopalavra = ""


    def exibeBoneco(self, erros):
        if erros == 0:
            print("------------")
            print("|          |")
            print("|           ")
            print("|           ")
            print("|           ")
            print("|           ")
            print("|           ")
            print("|           ")
        elif erros == 1:
            print("------------")
            print("|          |")
            print("|          O")
            print("|           ")
            print("|           ")
            print("|           ")
            print("|           ")
            print("|           ")
        elif erros == 2:
            print("------------")
            print("|          |")
            print("|          O")
            print("|          |")
            print("|           ")
            print("|           ")
            print("|           ")
            print("|           ")
        elif erros == 3:
            print("------------")
            print("|          |")
            print("|          O")
            print("|         -|")
            print("|           ")
            print("|           ")
            print("|           ")
            print("|           ")
        elif erros == 4:
            print("------------   ")
            print("|          |   ")
            print("|          O   ")
            print("|         -|-  ")
            print("|              ")
            print("|              ")
            print("|              ")
            print("|              ")
        elif erros == 5:
            print("------------   ")
            print("|          |   ")
            print("|          O   ")
            print("|         -|-  ")
            print("|         /    ")
            print("|              ")
            print("|              ")
            print("|              ")
        elif erros == 6:
            print("------------   ")
            print("|          |   ")
            print("|          O   ")
            print("|         -|-  ")
            print("|         / \  ")
            print("|              ")
            print("|   Lamento, Você Perdeu")
            print("|              ")
        erros = 0


    def verificaLetra(self, letrajogada):
        return 0