def roman_to_int_reverse(s: str) -> int:
	"""
	Dictionary mapping Roman numerals to their values
	:param roman: str
	:return: total: int
	"""

	roman_values = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	total = 0
	prev_value = 0

	# Iterate through the Roman numeral string from right to left
	for numeral in reversed(s.upper()):
		current_value = roman_values[numeral]

		# If the current value is greater than or equal to the previous value,
		# add it to the total (like in "VI = 6)
		if current_value >= prev_value:
			total += current_value
		# If the current value is less than the previous value,
		#subtract it from the total (like in "IV" = 4)
		else:
			total -= current_value

		prev_value = current_value

	return  total

