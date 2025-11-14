# tests/test_roman_numerals.py

import pytest

from reversed_roman_numerals import roman_to_int_reverse
from roman_numerals import roman_to_int


# ----------------------------
# Valid numerals (reverse impl)
# ----------------------------
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
        ("MMMCMXCIX", 3999),  # common "max" Roman numeral
    ],
)
def test_roman_to_int_reverse(roman: str, expected: int) -> None:
    """roman_to_int_reverse (right-to-left) should return correct integer values."""
    assert roman_to_int_reverse(roman) == expected


# ----------------------------------
# Both implementations must match
# ----------------------------------
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
        "MMMCMXCIX",
    ],
)
def test_both_implementations_match(roman: str) -> None:
    """
    For valid Roman numerals, both algorithms
    should return the same result.
    """
    assert roman_to_int(roman) == roman_to_int_reverse(roman)


# ----------------------------------
# Lowercase and surrounding whitespace
# ----------------------------------
@pytest.mark.parametrize(
    "roman, expected",
    [
        ("ix", 9),
        ("  ix", 9),
        ("ix  ", 9),
        ("  mcmxciv  ", 1994),
        ("lviii", 58),
    ],
)
def test_lowercase_and_whitespace(roman: str, expected: int) -> None:
    """Both functions should handle lowercase and surrounding spaces."""
    assert roman_to_int(roman) == expected
    assert roman_to_int_reverse(roman) == expected


# ----------------------------------
# Invalid characters must raise ValueError
# ----------------------------------
@pytest.mark.parametrize(
    "roman",
    [
        "",
        " ",       # only spaces
        "A",
        "ICXZ",    # contains Z
        "X!",      # punctuation
        "MMX  V",  # internal space
    ],
)
def test_invalid_characters_raise_value_error(roman: str) -> None:
    """Invalid strings (empty or bad chars) should raise ValueError."""
    with pytest.raises(ValueError):
        roman_to_int(roman)

    with pytest.raises(ValueError):
        roman_to_int_reverse(roman)


# ----------------------------------
# Non-string input must raise TypeError
# ----------------------------------
@pytest.mark.parametrize(
    "value",
    [
        123,
        3.14,
        None,
        ["X"],
        {"roman": "X"},
    ],
)
def test_non_string_input_raises_type_error(value) -> None:
    """Passing non-string types should raise TypeError."""
    with pytest.raises(TypeError):
        roman_to_int(value)  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        roman_to_int_reverse(value)  # type: ignore[arg-type]
