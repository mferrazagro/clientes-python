# View - o que vai para o usuário do sistema
usuario_digitado = input("Informe o seu usuário: ")
senha_digitado = input("Informe sua senha:  ")

# Model - O que vem do banco de dados (BD)
usuario_BD = 'joao'
senha_BD = '123'

# Controller - a validação
if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
    print("pode entrar")
else: 
    print("usuário ou senha inválido")
