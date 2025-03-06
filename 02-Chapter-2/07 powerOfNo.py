def power_using_operator(base, exponent):
    return base ** exponent  # Using the exponentiation operator '**'

def power_using_pow(base, exponent):
    return pow(base, exponent)  # Using the built-in pow() function

def power_using_loop(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result  # Handling negative exponent

def power_using_recursion(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power_using_recursion(base, exponent - 1)
    else:
        return 1 / power_using_recursion(base, -exponent)  # Handling negative exponent

def power_using_math_pow(base, exponent):
    import math
    return math.pow(base, exponent)  # Using the math module's pow() function

def power_using_modular_exponentiation(base, exponent, mod):
    result = 1
    base = base % mod  # Handle large base values
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd, multiply base with result
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod  # Square the base
    return result

# Example usage:
base = 2
exponent = 3
mod = 1000000007

print("Using '**' operator:", power_using_operator(base, exponent))
print("Using pow() function:", power_using_pow(base, exponent))
print("Using loop:", power_using_loop(base, exponent))
print("Using recursion:", power_using_recursion(base, exponent))
print("Using math.pow() function:", power_using_math_pow(base, exponent))
print("Using modular exponentiation:", power_using_modular_exponentiation(base, exponent, mod))
