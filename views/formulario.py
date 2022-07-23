# View - o que vai para o usuário do sistema

def formulario_login():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("Informe sua senha:  ")
    usuario_completo = [usuario_digitado , senha_digitado]
    return usuario_completo

def exibir_mensagem(texto):
    print("\n\n")
    print("==============")
    print(texto)
    print("\n\n")
    print("==============")

def menu():
    print("1 - Cadastrar novo cliente")
    print("2 - Para listar todos os clientes")
    print("3 - Para sair")
    opcao = input("Digite a opção \n")
    return opcao

def cadastro_clientes():
    nome = input("Informe o nome:   ")
    telefone = input("Informe o telefone:   ")
    cliente = [nome, cliente]
    return cliente