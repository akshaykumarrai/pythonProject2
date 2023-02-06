
with open("miracle_in_the_andes.txt","r",encoding='utf-8') as file:
    book =  file.read()
#
print(type(book))

print(book.count("Chapter"))
import re

pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern,book)
#print(findings)
#sentences where love was matched
pattern1 = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z] [^.]*.")
findings1 = re.findall(pattern1,book)
#print(findings1)
#print(type(findings1))
#most used words


#print(book.split())
pattern2 = re.compile("[a-zA-Z]+")
findings2 = re.findall(pattern2,book.lower())
d ={}
for word in findings2:
    if word not in d.keys():
        d[word] = 1

    else:
        d[word] += 1

d_list = [(value,key) for (key,value) in d.items()]
#print(sorted(d_list,reverse = True))

#extract titles

pattern3 = re.compile("[a-zA-Z ,]+\n\n") #"([a-zA-Z ]+)\n\n"
findings3 = re.findall(pattern3,book)
findings3=[item.strip("\n\n") for item in findings3]
print(findings3)


#print the occurences of the word

def find(w):
    pattern2 = re.compile("[a-zA-Z]+")
    findings2 = re.findall(pattern2, book.lower())
    d = {}
    for word in findings2:
        if word not in d.keys():
            d[word] = 1

        else:
            d[word] += 1
    try:
        return d[w]
    except:
        return f"The book does not contain the word {w}"

print(find("hate"))





