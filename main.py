string = 'abxabcabcaby' # - i
pattern = 'abcaby' # - j

def check(lookup_arr):
	i, j = 0, 0
	while i < len(lookup_arr):
		if string[i] == pattern[j]:
			i += 1
			j += 1
		else:
			j -= 1
			j = lookup_arr[j]
			continue

def setupLookup():
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

arr = setupLookup()
check(arr)
print(arr)

