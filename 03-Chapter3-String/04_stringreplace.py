name = input("Enter your name: ")
print(f"Good Morning, {name}")

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

personalized_letter = letter.replace("<|Name|>", name).replace("<|Date|>", "24 Sep 2050")
harsh_letter = letter.replace("<|Name|>", "Harsh").replace("<|Date|>", "24 Sep 2050")

print(personalized_letter)
print(harsh_letter)
