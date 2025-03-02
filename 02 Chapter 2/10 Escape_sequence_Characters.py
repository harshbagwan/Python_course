def escape_sequences_demo():
    print("Hello\nWorld")  # Newline (Most used)
    # Input: "Hello\nWorld" → Output:
    # Hello
    # World

    print("Hello\tWorld")  # Tab (Most used)
    # Input: "Hello\tWorld" → Output: "Hello    World"

    print("Helloo\bWorld")  # Backspace (Removes last 'o') (Rarely used)
    # Input: "Helloo\bWorld" → Output: "HelloWorld"

    print("Hello\rWorld")  # Carriage return (Overwrites 'Hello' with 'World') (Rarely used)
    # Input: "Hello\rWorld" → Output: "World"

    print("Hello\fWorld")  # Form feed (New page break in some printers) (Rarely used)
    # Input: "Hello\fWorld" → Output: "Hello (form feed) World"

    print("Hello\\World")  # Backslash (Most used)
    # Input: "Hello\\World" → Output: "Hello\World"

    print("Hello\'World")  # Single quote (Commonly used)
    # Input: "Hello\'World" → Output: "Hello'World"

    print('Hello\"World')  # Double quote (Commonly used)
    # Input: "Hello\"World" → Output: "Hello"World"

    print("Hello\aWorld")  # Bell sound (May produce a beep sound in some systems) (Rarely used)
    # Input: "Hello\aWorld" → Output: "HelloWorld" (May produce a beep sound)

    print("Hello\vWorld")  # Vertical tab (Moves text down but keeps horizontal position) (Rarely used)
    # Input: "Hello\vWorld" → Output: "Hello (vertical space) World"

    print("Hello\x48World")  # Hexadecimal character (\x48 is 'H', outputs 'Helloworld') (Advanced usage)
    # Input: "Hello\x48World" → Output: "HelloHWorld"

    print("Hello\u0048World")  # Unicode character (\u0048 is 'H', outputs 'Helloworld') (Advanced usage)
    # Input: "Hello\u0048World" → Output: "HelloHWorld"

    print("Hello\U00000048World")  # Extended Unicode character (\U00000048 is 'H', outputs 'Helloworld') (Advanced usage)
    # Input: "Hello\U00000048World" → Output: "HelloHWorld"

    print("Hello\N{GREEK CAPITAL LETTER ALPHA}World")  # Named Unicode character (Outputs 'HelloΑWorld') (Advanced usage)
    # Input: "Hello\N{GREEK CAPITAL LETTER ALPHA}World" → Output: "HelloΑWorld"

escape_sequences_demo()
