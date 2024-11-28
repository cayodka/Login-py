import os

# usuarios q estão definidos
usuarios = {
    "cayo": "123"
}

# os e a biblioteca q possibilita mexer nos sistemas internos, ai ta verificando se e win ou linux para limpar o terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função do login
def login():
    clear_terminal()
    print("sistema de login boladao da aula do ogai")
    
    username = input("Usuario: ")
    password = input("Senha: ")

    # aqui verifica se está certo ou errado
    if username in usuarios and usuarios[username] == password:
        # aqui e login basico onde, se usuario e senha forem os mesmo fornecidos em usuarios ent vai dar confere no login
        clear_terminal()
        print(f"Bem-vindo, {username}!")
    else:
        # agora aqui, so vai funcionar se os dados estiverem errados
        clear_terminal()
        print("Haha errou, faz denovo.")

login()
