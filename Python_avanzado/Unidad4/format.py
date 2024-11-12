#Programa que valida el formato del nombre de usuario

import re

'''name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(",")
    name = f"{first} {last}"
print(f"hello, {name}")'''

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
    
print(f"hello, {name}")