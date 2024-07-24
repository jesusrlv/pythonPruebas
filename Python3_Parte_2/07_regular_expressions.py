## regular expression ##

import re

my_string = "esta lección es la 7: Lección es Expresiones reg."
my_string_2 = "SI, esta lección es la 7: Exp. reg."

match = re.match("esta lección es",my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

span = match.span()
print(span) #encuentra entre qué caracteres está

match = print(re.match("esta lección es", my_string_2))
print(match)


print(re.match("esta lección es",my_string, re.I))
print(re.match("esta lección es",my_string_2))
print(re.match("Exp. reg.",my_string, re.I))

#search

search = re.search("lección",my_string,re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

#findall

findall = re.findall("lección",my_string,re.I) #lo guarda en una tupla o lista y busca en mayúsculas o minúsculas
print(findall)

#split

split = re.split(":",my_string) #divide a partir del valor que encuentre
print(split)

#sub

sub = re.sub("Expresiones reg.", "ExPrEsIoNeS REGULARES",my_string)
print(sub)

sub = re.sub("[l|L]ección.", "LECCIONES",my_string)
print(sub)

# patrones personalizados - patterns

pattern = r"[lL]ección"
print(re.findall(pattern,my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern,my_string))

pattern = r"[0-9]"
print(re.findall(pattern,my_string))
print(re.search(pattern,my_string))

pattern = r"\d"
print(re.findall(pattern,my_string))

pattern = r"\D"
print(re.findall(pattern,my_string))

pattern = r"[l].*"
print(re.findall(pattern,my_string))

#email validation

email ="jesusrlv@zac.com.mx"
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.findall(pattern,email))