# Find a circular sequence of seven 0's and seven 1 's such that all
# 4-digit binary numbers except 0000 and 1111 appear as blocks of
# the sequence.

import random
import networkx as nx
import matplotlib.pyplot as plt


# Função que gera uma sequência aleatória de sequences
def generate_random_sequence(number_of_sequences: int):

    # Inicializa uma lista vazia
    sequence = []

    multiplier = number_of_sequences // 2

    number_one = "1" * multiplier
    number_zero = "0" * multiplier

    sequence = number_one + number_zero
    sequence = list(sequence)

    # Shuffle the string
    random.shuffle(sequence)

    sequence = "".join(sequence)

    return sequence


def create_directed_graph(sequence: str, sequences: list):

    # Removendo o primeiro digito de cada sequência
    for i in range(len(sequences)):
        sequences[i] = sequences[i][1:]

    # Criando um grafo direcionado
    G = nx.DiGraph()

    # Criando uma lista com os arcos do grafo, onde o primeiro elemento é o nó de origem e o seguinte é o nó de destino
    arcs = []
    i = 0
    while len(arcs) <= len(sequences):
        if i == 0:
            arcs.append((sequences[i], sequences[i]))
            i += 1
            continue
        if i == len(sequences) - 1:
            temp_tuple = (sequences[i], sequences[0])
            if temp_tuple in arcs:
                return main(n)
            arcs.append(temp_tuple)
            break
        temp_tuple = (sequences[i], sequences[i + 1])
        if temp_tuple in arcs:
            return main(n)
        arcs.append(temp_tuple)
        i += 1

    # Adicionando os arcos ao grafo
    i = 0
    for arc in arcs:
        G.add_edge(arc[0], arc[1])
        i += 1

    if len(G.edges()) != 2**n:
        return main(n)

    print(sequence)
    print(len(G.edges()))
    print(G.edges())

    pos = nx.circular_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

    print("O grafo é euleriano? R: " + str(nx.is_eulerian(G)))

    plt.box(False)
    plt.show()

    return


def main(n):
    number_of_sections = 2**n
    # Gera uma sequência aleatória de 2**n bits
    sequence = generate_random_sequence(number_of_sections)

    # Verifica se a sequência gerada é válida
    if len(sequence) != 2**n:
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
            tmp_str = "".join(tmp_arr)
            sequences.append(tmp_str)

    # Se o tamanho da lista for diferente de 2**n bits, significa que alguma sequência de n bits está duplicada
    # e chama novamente a função até que todas as sequências sejam únicas
    if len(sequences) != 2**n:
        return main(n)

    create_directed_graph(sequence, sequences)

    return


n = int(input("Enter value of n: "))
main(n)
