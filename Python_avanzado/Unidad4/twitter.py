#Programa que extrae de una url el nombre de perfil del usuario
import re


url = input("URL: ").strip()

'''username = url.replace("https://twitter.com/", "")'''
'''username = url.removeprefix("https://twitter.com/")'''
#() hace que los datos dentro sean opcionales
'''username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)'''
'''print(f"Username: {username}")'''

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

