# 🏛️ Roman Numerals → Integer Converter (with Tests)

A small but polished Python project that converts **Roman numerals** into integers using **two different O(n) algorithms**:

- A **left-to-right** scan
- A **right-to-left** scan

Both implementations are fully tested with `pytest`, including edge cases and input validation.  
This repo is meant to showcase **clear algorithmic thinking**, **clean code**, and **professional testing practice**.

---

## ✨ Features

- Convert Roman numerals like `III`, `IX`, `XL`, `LVIII`, `MCMXCIV`, `MMMCMXCIX` to integers.
- Two independent algorithms:
  - `roman_to_int` (left-to-right)
  - `roman_to_int_reverse` (right-to-left)
- Handles:
  - Uppercase and lowercase input (e.g. `"ix"`, `"mcmxciv"`)
  - Leading/trailing whitespace (e.g. `"  IX  "`)
- Validates input:
  - Raises `ValueError` for invalid characters (e.g. `"A"`, `"X!"`, `""`)
  - Raises `TypeError` for non-string input (e.g. `123`, `None`)

---

## 🧠 Algorithms & Time Complexity

Both algorithms run in **O(n)** time where `n` is the length of the Roman numeral string.

### 1. Left-to-right algorithm (`roman_to_int`)

File: `roman_numerals.py`

Idea:

- Scan the string from **left to right**.
- At each position, compare the current symbol with the **next** one:
  - If the current value is **less than** the next → subtraction case  
    e.g. `"IV"` → `5 - 1 = 4`
  - Otherwise → add normally  
    e.g. `"VI"` → `5 + 1 = 6`

Each character is processed at most once (sometimes in a pair for subtraction), so the complexity is O(n).

### 2. Right-to-left algorithm (`roman_to_int_reverse`)

File: `reversed_roman_numerals.py`

Idea:

- Scan from **right to left**.
- Keep track of the **previous value** you saw.
- For each symbol:
  - If current ≥ previous → **add** it.
  - If current < previous → **subtract** it.

This style often matches how humans mentally parse numerals like `MCMXCIV`.  
Again, each character is visited once → O(n).

---

## 📂 Project Structure

```text
roman_numerals/
├── README.md
├── roman_numerals.py          # Main left-to-right implementation + shared constants
├── reversed_roman_numerals.py # Right-to-left implementation (reuses core logic)
├── roman_numerals_plan.py     # Thinking / algorithm plan (problem breakdown)
└── tests/
    └── test_roman_numerals.py # Pytest suite for both implementations
