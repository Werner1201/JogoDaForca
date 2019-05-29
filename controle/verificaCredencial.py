from modelo.admin import Admin

instadmin = Admin()

def controleLogin(nome, senha):
    if instadmin.verifica(nome, senha):
        return True
    else:
        return False

