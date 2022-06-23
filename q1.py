# Find a circular sequence of seven 0's and seven 1 's such that all
# 4-digit binary numbers except 0000 and 1111 appear as blocks of
# the sequence.

import random


# Função que gera uma sequência aleatória de bits
def generate_random_sequence(number_of_bits: int):

    # Inicializa uma lista vazia
    sequence = []

    # Loop que gera um número aleatório de 0 a 1 para cada número de bits e adiciona na lista
    for i in range(number_of_bits):
        sequence.append(str(random.randint(0, 1)))

    # Transforma a lista em uma string
    sequence = "".join(sequence)

    # Verifica se a sequência gerada é válida e a retorna
    if sequence.count("0") == 7 and sequence.count("1") == 7:
        return sequence

    # Caso não seja válida, chama a função novamente
    return generate_random_sequence(number_of_bits)


def main():
    # Gera uma sequência aleatória de 14 bits
    sequence = generate_random_sequence(14)

    # Verifica se a sequência gerada é válida
    if len(sequence) != 14:
        print("Sequence must be 14 characters long.")
        return

    # Inicializa uma lista para armazenar as sequências de 4 bits
    sequences = []

    # Loop que verifica se existe uma sequência de 4 bits duplicada
    for i in range(0, len(sequence)):
        j = i
        tmp_arr = []
        while j != (i + 4) % len(sequence):
            tmp_arr.append(sequence[j])
            j = (j + 1) % len(sequence)
        if tmp_arr not in sequences:
            sequences.append(tmp_arr)

    # Se o tamanho da lista for diferente de 14 bits, significa que alguma sequência de 4 bits está duplicada
    # e chama novamente a função até que todas as sequências sejam únicas
    if len(sequences) != 14:
        return main()

    diff_array = [["0", "0", "0", "0"], ["1", "1", "1", "1"]]

    # Caso exista sequências 0000 e 1111, apague da lista
    if diff_array[0] in sequences:
        sequences.remove(["0", "0", "0", "0"])
    if diff_array[1] in sequences:
        sequences.remove(["1", "1", "1", "1"])

    print(sequence)
    for reading in sequences:
        print(reading)

    return


main()
