# Demonstrating most used string functions in Python

def string_functions_demo():
    text = "  Hello, Python World!  "
    print("Original text:", text)
    
    # 1. strip(): Removes leading and trailing whitespaces
    print("Strip:", text.strip())
    
    # 2. lower(): Converts string to lowercase
    print("Lowercase:", text.lower())
    
    # 3. upper(): Converts string to uppercase
    print("Uppercase:", text.upper())
    
    # 4. replace(): Replaces a substring with another substring
    print("Replace 'Python' with 'Programming':", text.replace("Python", "Programming"))
    
    # 5. split(): Splits string into a list
    print("Split by space:", text.split())
    
    # 6. join(): Joins elements of a list into a single string
    words = ["Join", "these", "words"]
    print("Join words with '-':", "-".join(words))
    
    # 7. find(): Finds the first occurrence of a substring
    print("Find 'Python':", text.find("Python"))
    
    # 8. count(): Counts occurrences of a substring
    print("Count 'o':", text.count("o"))
    
    # 9. startswith(): Checks if the string starts with a given substring
    print("Starts with 'Hello':", text.startswith("Hello"))
    
    # 10. endswith(): Checks if the string ends with a given substring
    print("Ends with 'World!':", text.endswith("World!"))
    
    # 11. isdigit(): Checks if the string contains only digits
    num_str = "12345"
    print("Is digit:", num_str.isdigit())
    
    # 12. isalpha(): Checks if the string contains only alphabets
    alpha_str = "Python"
    print("Is alpha:", alpha_str.isalpha())
    
    # 13. isalnum(): Checks if the string contains only alphanumeric characters
    alnum_str = "Python123"
    print("Is alphanumeric:", alnum_str.isalnum())
    
    # 14. capitalize(): Capitalizes the first letter of the string
    print("Capitalize:", text.capitalize())
    
    # 15. title(): Converts string to title case
    print("Title Case:", text.title())
    
string_functions_demo()
 