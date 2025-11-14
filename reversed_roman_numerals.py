
"""
Roman numeral → integer conversion (right-to-left algorithm).

This module exposes:
- roman_to_int_reverse(): alternative conversion function

It reuses:
- ROMAN_VALUES
- _normalize_and_validate
from roman_numerals.py to keep behavior consistent.
"""

from roman_numerals import ROMAN_VALUES, _normalize_and_validate


def roman_to_int_reverse(s: str) -> int:
	"""
	Dictionary mapping Roman numerals to their values
	:param roman: str
	:return: total: int
	"""

	s = _normalize_and_validate(s)

	total = 0
	prev_value = 0

	# Iterate through the Roman numeral string from right to left
	for numeral in reversed(s):
		current_value = ROMAN_VALUES[numeral]

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

