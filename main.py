################################################
# Advanced Analysis of Algorithms
# Project: Motif finding using KMP Algorithm
# Members:
#   Hitesh Arora (50489713),
#   Sulav Regmi (50211843)
# Dr. Huang
# ##############################################
#


def readFromFile():
    sequences = []
    line_idx = 0
    with open('sequence.fasta') as f:
        content = f.read()
        for line in content.splitlines():
            if line_idx % 2 == 0:
                line_idx += 1
                continue
            else:
                line_idx += 1
                sequences.append(line)
    return sequences


def check(lookup_arr, result, pattern, string):
    i, j = 0, 0
    while j < len(lookup_arr):
        if i < len(string):
            if string[i] == pattern[j]:
                result += string[i]
                i += 1
                j += 1
            else:
                if j != 0:
                    j -= 1
                    j = lookup_arr[j]
                    continue
                else:
                    i += 1
                    continue
        else:
            break
    return result[-len(pattern):]


def setupLookup(pattern):
    i, j = 1, 0
    arr = [0] * len(pattern)

    while i < len(pattern):
        if pattern[j] == pattern[i]:
            arr[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j -= 1
                j = arr[j]
                continue
            else:
                arr[i] = 0
                i += 1
                continue
    return arr

sequences = readFromFile()


idx = 0
while idx < len(sequences[0]) - 15:
    ptrn = sequences[0][idx:(idx+15)]

    res = ''
    arr = setupLookup(ptrn)

    matched = []
    for sequence in range(1, len(sequences)):
        matched.append(check(arr, res, ptrn, sequences[sequence]))

    if (all(x == ptrn for x in matched)):
        print(ptrn, ' matched in all sequences.')
        break
    else:
        idx += 1
        if idx == len(sequences[0]) - 16:
            print('Match not found in all sequences!')
        continue
