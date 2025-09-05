def romanToInt(s: str) -> int:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    i = 0
    
    while i < len(s):
        # If current value < next value, it's a subtractive case
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            total += roman[s[i + 1]] - roman[s[i]]
            i += 2  # Skip the next character as well
        else:
            total += roman[s[i]]
            i += 1
    
    return total
