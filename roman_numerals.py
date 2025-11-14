"""
Roman numeral → integer conversion (left-to-right algorithm).

This module exposes:
- roman_to_int(): main conversion function
- ROMAN_VALUES: dict of basic numeral values (reused by other modules)
"""

from typing import Dict

# Public constant so other modules (like reversed_roman_numerals.py) can reuse.
ROMAN_VALUES: Dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def _normalize_and_validate(s: str) -> str:
    """
    Normalize and validate a Roman numeral string.

    - Ensures input is a string, otherwise raises TypeError.
    - Strips leading/trailing whitespace.
    - Converts to uppercase (so 'ix' works like 'IX').
    - Ensures string is not empty.
    - Ensures all characters are valid Roman symbols.

    Note: This does NOT fully validate Roman numeral grammar
    (e.g. 'IC' is still accepted). It only checks allowed characters.
    """
    if not isinstance(s, str):
        raise TypeError(f"Roman numeral must be a string, got {type(s).__name__}")

    s = s.strip().upper()

    if not s:
        raise ValueError("Roman numeral string cannot be empty")

    for ch in s:
        if ch not in ROMAN_VALUES:
            raise ValueError(f"Invalid Roman numeral character: {ch!r}")

    return s


def roman_to_int(string_of_roman_numerals: str) -> int:
    """
    Convert a Roman numeral string into an integer using a left-to-right scan.

    Rules:
    - If a smaller value comes before a larger value (e.g. IV),
      we subtract the smaller from the larger.
    - Otherwise, we simply add the value (e.g. VI = 5 + 1).

    Examples:
    - 'III'      -> 3
    - 'IV'       -> 4
    - 'IX'       -> 9
    - 'LVIII'    -> 58
    - 'MCMXCIV'  -> 1994

    Time complexity: O(n), where n is the length of the string.
    """
    s = _normalize_and_validate(string_of_roman_numerals)

    total = 0
    i = 0

    while i < len(s):
        current = ROMAN_VALUES[s[i]]

        # Look ahead to the next symbol if it exists
        if i + 1 < len(s):
            next_val = ROMAN_VALUES[s[i + 1]]

            # Subtraction case: current < next (e.g. IV, IX, XL, etc.)
            if current < next_val:
                total += next_val - current
                i += 2
                continue

        # Normal case: just add current value
        total += current
        i += 1

    return total


if __name__ == "__main__":
    print(roman_to_int("MCMXCIV"))
    print(roman_to_int("IX"))
    print(roman_to_int("XL"))
