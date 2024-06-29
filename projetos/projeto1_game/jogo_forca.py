import random

def escolherPalavra(lista_palavras: list):
    palavra_selecionada = random.choice(lista_palavras)
    return palavra_selecionada

def atualizarPalavra(palavra: str, underscores: str, caracter: str):
    letras_adivinhadas = underscores.split()

    for i, letra in enumerate(palavra):
        if letra == caracter:
            letras_adivinhadas[i] = caracter
    palavra_atualizada = ' '.join(letras_adivinhadas)

    return palavra_atualizada

def menu():
    palavras_possiveis = ['banana', 'flamengo', 'pescador', 'surfista','jesus']

    palavra_escolhida = escolherPalavra(palavras_possiveis)

    max_tentativas = len(palavra_escolhida)

    palavra_atualizada = ' '.join(['_'] * max_tentativas)

    palavra_adivinhada = None

    print('--------------- JOGO FORCA --------------\n')
    while max_tentativas:
        print(palavra_atualizada)

        if max_tentativas > 0 and palavra_adivinhada == palavra_escolhida:
            print('\nVocê venceu!!')
            print(f'A palavra escolhida foi: {palavra_escolhida}')
            break

        tentativa = str(input(f'\nDigite uma letra: \nR: '))
        tentativa = tentativa.lower()

        if tentativa in palavra_escolhida:
            palavra_atualizada = atualizarPalavra(palavra_escolhida, palavra_atualizada, tentativa)
            palavra_adivinhada = palavra_atualizada.replace(' ','')
            print(palavra_atualizada)

            max_tentativas -= 1
            print(f'\nTentativas restantes: {max_tentativas}')
        else:
            print('\nEsta letra não consta na palavra.')
            max_tentativas -= 1
            print(f'\nTentativas restantes: {max_tentativas}')

    if palavra_adivinhada == palavra_escolhida:
        print('\nVocê venceu!!')
        print(f'A palavra escolhida foi: {palavra_escolhida}')
    else:
        print('Você perdeu!')
        print(f'A palavra escolhida foi: {palavra_escolhida}')

if __name__ == '__main__':
    menu()
