usuarios = {
    "cayo" : "123"
}
def login():
    usarname = input("fala seu usuario meu bom: ")
    password = input("agora senha meu querido: ")
    if usarname in usuarios and usuarios[usarname] == password:
        print(f"login feito, {usarname}!")
    else :
        print(f"login nao feito, {usarname} é mó comedia")
login()