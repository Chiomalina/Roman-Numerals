from typing import List

# ============================
# ROMAN → INTEGER: THINKING PLAN
# ============================

# TODO 0: Restate the Problem in My Own Words
#   - Input: a string s representing a Roman numeral (e.g. "MCMXCIV").
#   - Output: an integer that is the numeric value of s.
#   - Goal: Mimic how a human reads Roman numerals: go from left to right,
#           usually adding values, but sometimes subtracting when a smaller
#           numeral comes before a larger one.

# TODO 1: Understand the Roman Numeral System
#   a) What does each symbol represent (I, V, X, L, C, D, M)?
#      - I = 1
#      - V = 5
#      - X = 10
#      - L = 50
#      - C = 100
#      - D = 500
#      - M = 1000
#   b) How are Roman numerals typically written?
#      - Normally, symbols are written from largest to smallest from left to right,
#        and we just add all the values.
#      - The exception is when a smaller symbol appears immediately before a larger
#        one (like "IV" or "IX"). In that case, the smaller value is subtracted
#        from the larger one instead of added.
#   c) What are the special “subtractive” cases?
#      - Common examples: IV, IX, XL, XC, CD, CM
#      - Pattern: a smaller numeral directly before a larger numeral means:
#          value = (larger − smaller)
#        e.g. I before V or X, X before L or C, C before D or M.

# TODO 2: Design My Data Representation
#   a) How will I store the value of each symbol?
#      - Use a dictionary mapping each character to its integer value, e.g.:
#          values = {
#              "I": 1, "V": 5, "X": 10, "L": 50,
#              "C": 100, "D": 500, "M": 1000,
#          }
#   b) What should happen if s contains an invalid character?
#      - For now, I can assume the input is always a valid Roman numeral.
#      - (Later, I could add a check and raise a ValueError for unknown symbols.)

# TODO 3: Simulate the Algorithm by Hand on Examples
#   # Goal: Train my brain to think like the algorithm (left-to-right with lookahead).
#   a) Example 1: "III"
#      - Symbols: I, I, I (each = 1)
#      - Process left to right:
#          total = 0
#          see I → add 1 → total = 1
#          see I → add 1 → total = 2
#          see I → add 1 → total = 3
#      - Result: 3
#   b) Example 2: "IV"
#      - Symbols: I (1), V (5)
#      - Look at I and peek at the next symbol V:
#          current = 1, next = 5
#          since 1 < 5 → subtractive pair
#          add (5 − 1) = 4 to total
#          skip both characters (we’ve processed the pair)
#      - Result: 4
#   c) Example 3: "IX"
#      - Symbols: I (1), X (10)
#      - Look at I and next X:
#          current = 1, next = 10
#          since 1 < 10 → subtractive pair
#          add (10 − 1) = 9
#          skip both characters
#      - Result: 9
#   d) Example 4: "LVIII"
#      - Symbols: L (50), V (5), I (1), I (1), I (1)
#      - Process step by step:
#          total = 0
#          L → no larger symbol after it → add 50 → total = 50
#          V → next is I (1), and 5 > 1 → not subtractive → add 5 → total = 55
#          I → next is I (1), and 1 >= 1 → not subtractive → add 1 → total = 56
#          I → next is I (1), and 1 >= 1 → add 1 → total = 57
#          I → no next symbol → add 1 → total = 58
#      - Result: 58
#   e) Advanced Example: "MCMXCIV"
#      - String:  M   C   M   X   C   I   V
#      - Values: 1000 100 1000 10 100  1   5
#      Step-by-step with index i:
#      i = 0:
#        current = M (1000), next = C (100)
#        1000 > 100 → not subtractive
#        add 1000 → total = 1000
#        i = 1
#      i = 1:
#        current = C (100), next = M (1000)
#        100 < 1000 → subtractive pair "CM"
#        add (1000 − 100) = 900 → total = 1900
#        skip both → i = 3
#      i = 3:
#        current = X (10), next = C (100)
#        10 < 100 → subtractive pair "XC"
#        add (100 − 10) = 90 → total = 1990
#        skip both → i = 5
#      i = 5:
#        current = I (1), next = V (5)
#        1 < 5 → subtractive pair "IV"
#        add (5 − 1) = 4 → total = 1994
#        skip both → i = 7 (end)
#      Final result: 1994

# TODO 4: Break Down the General Algorithm (Left-to-Right)
#   a) What variables do I need?
#      - total: an integer accumulator for the final result.
#      - i: an index to walk through the string s.
#  TODO 4b:
#   b) Basic loop strategy:
#      - While i is still within the string (i < len(s)):
#          - Get the value of s[i] as current.
#          - If i + 1 is within bounds, also get the value of s[i + 1] as next_val.
#  TODO 4c:
#   c) How to detect a subtractive pair:
#      - If there is a next symbol (i + 1 < len(s)):
#          - current = values[s[i]]
#          - next_val = values[s[i + 1]]
#          - If current < next_val → this is a subtractive pair.
#   TODO 4d:
#   d) What to do in each case:
#      - Case 1: current < next_val (subtractive pair)
#          - Add (next_val − current) to total.
#          - Increase i by 2 (skip both characters).
#
#      - Case 2: current >= next_val, or there is no next symbol
#          - Add current to total.
#          - Increase i by 1 (move to the next character).

# TODO 5: Translate the Plan into Step-by-Step Code Structure
#   a) Function signature:
#      - Name: roman_to_int
#      - Input type: str (the Roman numeral string).
#      - Return type: int (the numeric value).
#
#   b) Inside the function:
#      - Step 1: define the dictionary "values" with symbol → value mappings.
#      - Step 2: initialize total = 0 and i = 0.
#      - Step 3: write a while loop: while i < len(s):
#      - Step 4: inside the loop:
#          - read current = values[s[i]]
#          - if i + 1 < len(s), read next_val = values[s[i + 1]]
#          - if current < next_val:
#                add (next_val − current) to total and i += 2
#            else:
#                add current to total and i += 1
#      - Step 5: after the loop, return total.

# TODO 6: Think About Edge Cases
#   a) Empty string "":
#      - Decide behavior: return 0 (simple), or raise an error.
#      - For now, returning 0 is acceptable if I assume valid input usually.
#
#   b) Single-character strings like "V" or "X":
#      - The loop should handle this: no next symbol, so we just add current.
#
#   c) Repeated symbols like "III" or "XXX":
#      - Each character is processed one by one, always as a normal (non-subtractive) case.
#
#   d) Largest typical Roman numerals like "MMMCMXCIX" (3999):
#      - The same logic works; there is nothing special to change in the algorithm.

# TODO 7: Testing Plan
#   a) Prepare test cases:
#      - "III"      → 3
#      - "IV"       → 4
#      - "IX"       → 9
#      - "LVIII"    → 58
#      - "MCMXCIV"  → 1994
#
#   b) How to run tests:
#      - Option 1: write a simple main block that prints:
#            print(roman_to_int("III"))
#            print(roman_to_int("IV"))
#            ...
#      - Option 2: later, write proper unit tests using pytest.

# TODO 8: Complexity Reflection
#   a) Time complexity:
#      - Each character is visited at most once (or in pairs for subtractive cases),
#        so the time complexity is O(n), where n = len(s).
#
#   b) Space complexity:
#      - The dictionary of symbol values is constant size.
#      - Only a few integer variables are used (total, i, current, next_val).
#      - So the space complexity is O(1) (constant extra space).

# TODO 9: Clean Up
#   a) Remove any unused imports (e.g., typing.List if not used).
#   b) Make sure variable names are clear and descriptive (total, current, next_val, etc.).
#   c) Add a docstring to roman_to_int explaining what it does and how it works.
