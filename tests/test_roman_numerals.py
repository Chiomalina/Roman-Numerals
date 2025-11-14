import pytest

from reversed_roman_numerals import roman_to_int_reverse
from roman_numerals import roman_to_int

@pytest.mark.parametrize(
	"roman, expected",
	[
("I", 1),
		("II", 2),
		("III", 3),
		("IV", 4),
		("V", 5),
		("VI", 6),
		("IX", 9),
		("X", 10),
		("XL", 40),
		("L", 50),
		("XC", 90),
		("C", 100),
		("CD", 400),
		("D", 500),
		("CM", 900),
		("M", 1000),
		("LVIII", 58),
		("MCMXCIV", 1994),
		("XCIX", 99),
	]
)
def test_roman_to_int_reverse(roman: str, expected: int) -> None:
	"""roman_to_int_reverse (right-to-left) should return correct integer values."""
	assert roman_to_int_reverse(roman) == expected

@pytest.mark.parametrize(
	"roman",
	[
"I",
		"IV",
		"IX",
		"XL",
		"LVIII",
		"MCMXCIV",
		"XCIX",
	]
)
def test_both_implementations_match(roman: str) -> None:
	"""
	For valid Roman numerals, both algorithms
	should return the same result.
	"""
	assert roman_to_int(roman) == roman_to_int_reverse(roman)



