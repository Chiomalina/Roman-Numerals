from typing import List, Dict, Optional

def roman_to_int(string_of_roman_numerals: str) -> int:
	# step 1: Use a dictionary to map characters to its integer
	values = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	total = 0
	i = 0

	# Step 2: Initialize total and index
	total = 0
	i = 0

	# Step 3: Scan from left to right
	while i < len(string_of_roman_numerals):
		current = values[string_of_roman_numerals[i]]

		# Step 4: Check if there is a next symbol
		if i + 1 < len(string_of_roman_numerals):
			next_val = values[string_of_roman_numerals[i + 1]]

			# Subtraction case: current < next
			if current < next_val:
				total += next_val - current
				#Skip both characters
				i += 2
				continue

		# Normal case: just add current
		total += current
		i += 1
	return total




