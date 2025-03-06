# Demonstrating all major string methods in Python

def string_methods_demo():
    s = "  Hello, World!  "
    print("Original String:", s)
    
    # String modification methods
    print("Uppercase:", s.upper())  # Commonly used
    print("Lowercase:", s.lower())  # Commonly used
    print("Title Case:", s.title())  # Less common
    print("Capitalize:", s.capitalize())  # Commonly used
    print("Swapcase:", s.swapcase())  # Rarely used
    print("Strip:", s.strip())  # Commonly used
    print("LStrip:", s.lstrip())  # Less common
    print("RStrip:", s.rstrip())  # Less common
    
    # Search and replace methods
    print("Find 'World':", s.find("World"))  # Commonly used
    print("Index 'World':", s.index("World"))  # Less common
    print("Replace 'Hello' with 'Hi':", s.replace("Hello", "Hi"))  # Commonly used
    print("Count of 'l':", s.count("l"))  # Commonly used
    print("Starts with 'Hello':", s.startswith("Hello"))  # Less common
    print("Ends with '!':", s.endswith("!"))  # Less common
    
    # Splitting and joining
    print("Split:", s.split(", "))  # Commonly used
    print("Join with '-':", "-".join(["Hello", "World"]))  # Commonly used
    
    # Boolean check methods
    print("Is Alphanumeric:", s.isalnum())  # Rarely used
    print("Is Alphabetic:", s.isalpha())  # Less common
    print("Is Digit:", s.isdigit())  # Commonly used
    print("Is Lower:", s.islower())  # Less common
    print("Is Upper:", s.isupper())  # Less common
    print("Is Space:", s.isspace())  # Rarely used
    print("Is Title:", s.istitle())  # Rarely used
    
    # Formatting methods
    print("Centered with '*':", s.center(20, '*'))  # Rarely used
    print("Left Justified:", s.ljust(20, '*'))  # Rarely used
    print("Right Justified:", s.rjust(20, '*'))  # Rarely used
    
    # Encoding and decoding
    encoded = s.encode("utf-8")  # Advanced usage
    print("Encoded:", encoded)  # Advanced usage
    print("Decoded:", encoded.decode("utf-8"))  # Advanced usage

string_methods_demo()