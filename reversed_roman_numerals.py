def roman_to_int_reverse(s: str) -> int:
	"""
	Dictionary mapping Roman numerals to their values
	:param roman: str
	:return: total: int
	"""

	roman_values = {
		"I": 1,
	}

	total = 0
	prev_value = 0

	# Iterate through the Roman numeral string from right to left
	for numeral in reversed(s.upper()):
