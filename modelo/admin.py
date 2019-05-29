class Admin:

    def __init__(self):
        self.login = "admin"
        self.senha = "123456"

    def verifica(self, login, senha):
        if login == self.login and senha == self.senha:
            return True
        else:
            return False
