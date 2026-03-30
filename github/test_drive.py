# Write a program that converts a Roman numeral to an integer
def roman_to_int(s: str) -> int:
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s:
        value = roman_numerals[char]
        
        if prev_value < value:
            total += value - 2 * prev_value
        else:
            total += value
        
        prev_value = value
    
    return total

# Test the function with some examples
print(roman_to_int("III"))  # Output: 3
print(roman_to_int("IV"))   # Output: 4
print(roman_to_int("IX"))   # Output: 9
print(roman_to_int("LVIII")) # Output: 58
print(roman_to_int("MCMXC")) # Output: 1990