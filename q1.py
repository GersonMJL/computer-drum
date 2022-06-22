# Find a circular sequence of seven 0's and seven 1 's such that all
# 4-digit binary numbers except 0000 and 1111 appear as blocks of
# the sequence.

import random


def generate_random_sequence(number_of_bits: int):
    sequence = []
    for i in range(number_of_bits):
        sequence.append(str(random.randint(0, 1)))
    sequence = "".join(sequence)
    if sequence.count("0") == 7 and sequence.count("1") == 7:
        return sequence
    return generate_random_sequence(number_of_bits)


def main():
    sequence = generate_random_sequence(14)

    if len(sequence) != 14:
        print("Sequence must be 14 characters long.")
        return

    if sequence.count("0") != 7 or sequence.count("1") != 7:
        print("Sequence must contain 7 0's and 7 1's.")
        return

    # Create a list of all possible sequences of 4 digits of 0's and 1's inside sequence list
    sequences = []
    for i in range(0, len(sequence)):
        j = i
        tmp_arr = []
        while j != (i + 4) % len(sequence):
            tmp_arr.append(sequence[j])
            j = (j + 1) % len(sequence)
        if tmp_arr not in sequences:
            sequences.append(tmp_arr)

    if len(sequences) != 14:
        return main()

    sequences.remove(["0", "0", "0", "0"])
    sequences.remove(["1", "1", "1", "1"])

    for sequence in sequences:
        print(sequence)

    return


main()
