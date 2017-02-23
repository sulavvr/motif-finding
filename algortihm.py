### find pattern in text

# pattern string to array
# calculate index for pattern
	# first index - 0
	# start first index (j) second index (i)
	# while i != len
		# if pattern[j] == pattern[i]
			# arr[i] = j + 1
			# i++, j++
		# else if pattern[j] != pattern[i]
			# j != 0
				# j--
				# j = arr[j]
				# continue
			# j == 0
				# a[i] = 0
				# i++
				# continue

