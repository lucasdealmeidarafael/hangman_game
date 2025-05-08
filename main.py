import random

# Cria uma lista de palavras que serão sorteadas.
with open('word_list', 'r') as file:

    words = []
    for line in file:
        line_words = line.strip().split()
        words.extend(line_words)

# Escolhendo uma das palavras.
random_word = random.choice(words)

# String apenas com os traços, que representam as letras da palavra.
secret_word = '-' * len(random_word)


# Lista vazia para armazenar as letras que já foram faladas
letters = []

max_tentatives = 6

while True:
    # Mostra na tela a palavra secreta.
    print(secret_word)

    # É pedido ao jogador para digitar uma letra.
    chosse_letter = input("Digite uma letra: ")

    # Verificando se a letra já foi digitada.
    if chosse_letter in letters:
        print("Você já digitou essa letra. Tente outra letra por favor!")
        continue

    # Adicionar a letra a lista de letras digitadas.
    letters.append(chosse_letter)

    # Verificando se a letra digitada está na palavra sorteada.
    if chosse_letter in random_word:
        list = []
        for indice in range(len(random_word)):
            if chosse_letter == random_word[indice]:
                list.append(chosse_letter)
            else:
                list.append(secret_word[indice])

        secret_word = ''.join(list) # Se o jogador digitou a letra 'a' por exemplo teremos = a**a.

    else: # Essa letra não está na palavra sorteada.
        max_tentatives -= 1
        print(f'Letra não encontrada. Você tem mais {max_tentatives} tentativas')

    # Verificando se o jogador ganhou ou perdeu.
    if secret_word == random_word:
        print("Parabéns, você ganhou!!")
        break

    elif max_tentatives == 0:
        print(f'Você perdeu. A palavra era {random_word}.')
        break