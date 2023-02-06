
with open("miracle_in_the_andes.txt","r",encoding='utf-8') as file:
    book =  file.read()
#
print(type(book))

print(book.count("Chapter"))
import re

pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern,book)
print(findings)

