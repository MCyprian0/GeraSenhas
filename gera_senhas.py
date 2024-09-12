'''
GERADOR DE SENHAS SEGURAS - v 1.0
Autor: Mateus Cardoso Cypriano

Coisas que podem ser alteradas:
- o usuário passa a escolher se deseja que a senha tenha ou não maiúsculas, minúsculas, números
e caracteres especiais (talvez não)
- embelezamento do código para ficar mais bonito pros olhos
'''

import random
import string
from zoneinfo import reset_tzpath


# Função para gerar a senha
def gerar_senha(tamanho):
    # caracteres possíveis na senha (letras, números e especiais)
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Garantir pelo menos 1 caracter de cada tipo
    senha = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Completar a senha até o tamanho estipulado
    senha += random.choices(caracteres, k = tamanho - 4)

    # Embaralhar tudo
    random.shuffle(senha)

    # Senha gerada vai pra uma string
    return ''.join(senha)

while True:
    try:
        tamanho_senha = int(input("Digite a quantidade de caracteres desejada (Ex: 12): "))
        if tamanho_senha <= 4:
            raise ValueError("A quantidade de caracteres deve ser maior que 4")
        break

    except ValueError as ve:
        print(f"Ocorreu um erro: {ve}. Por favor, tente novamente.")

senha_gerada = gerar_senha(tamanho_senha)
print(f"Sua senha forte é: {senha_gerada}")
