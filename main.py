################################################
# Advanced Analysis of Algorithms
# Project: Motif finding using KMP Algorithm
# Members:
# 	Hitesh Arora (50489713),
# 	Sulav Regmi (50211843)
# Dr. Huang
# ##############################################

string_o = 'atgaccgggatactgatagaagaaaggttgggggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccgacccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaatacaataaaacggcgggatgagtatccctgggatgacttaaaataatggagtggtgctctcccgatttttgaatatgtaggatcattcgccagggtccga' # - i


string_t = 'gctgagaattggatgcaaaaaaagggattgtccacgcaatcgcgaaccaacgcggacccaaaggcaagaccgataaaggagatcccttttgcggtaatgtgccgggaggctggttacgtagggaagccctaacggacttaatataataaaggaagggcttataggtcaatcatgttcttgtgaatggatttaacaataagggctgggaccgcttggcgcacccaaattcagtgtgggcgagcgcaa'
string_th = 'cggttttggcccttgttagaggcccccgtataaacaaggagggccaattatgagagagctaatctatcgcgtgcgtgttcataacttgagttaaaaaatagggagccctggggcacatacaagaggagtcttccttatcagttaatgctgtatgacactatgtattggcccattggctaaaagcccaacttgacaaatggaagatagaatccttgcatactaaaaaggagcggaccgaaagggaag'


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
	return result[-len(pattern):]# == pattern

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

idx = 0
while idx < len(string_o) - 15:
	ptrn = string_o[idx:(idx+15)]

	res = ''
	arr = setupLookup(ptrn)

	matched_t = check(arr, res, ptrn, string_t)
	matched_th = check(arr, res, ptrn, string_th)

	if matched_t == ptrn and matched_th == ptrn:
		print(ptrn, ' matched in both sequence.')
		break
	else:
		idx += 1
		continue

# print(idx)




# res = ''
# arr = setupLookup()
# matched = check(arr, res)

# print(matched)

