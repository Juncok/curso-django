import requests
def buscar_avatar(usuario):
    url = 'https://api.github.com/users/' + usuario
    url_avatar = requests.get(url)
    return url_avatar.json()['avatar_url']

def nome_usuario():
    usuario = input("Digite um usuário: ")
    return usuario
while True:
    print(buscar_avatar(nome_usuario()))