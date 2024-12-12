import re

def naity(m):
  if re.fullmatch(r"\b[ABEKMHOPCTYX]{1}\d{3}[ABEKMHOPCTYX]{2}\s+\d{2,3}\b", m):
    return "chastny"
  elif re.fullmatch(r"\b[ABEKMHOPCTYX]{2}\d{3}\s\d{2,3}\b", m):
    return "taxi"
  else:
    return "ne znayu"
m = input()
result = naity(m)
print(result)


print (len(re.findall(r"\b[A-Za-zА-Яа-я]+\b", input())))


pismo = input()
poisk = re.findall(r"\b\d{2}\W\d{2}\W\d{2}\b", pismo)
redakcia = re.sub(r"\b\d{2}\W\d{2}\W\d{2}\b", "TBD", pismo)
print(redakcia)

text = input()
abbreviation_pattern = r'\b([А-ЯЁ]{2,}(?:s+[А-ЯЁ]{2,})*)\b'
abbreviations = re.findall(abbreviation_pattern, text)
print("find abbr:")
for abbr in abbreviations:
    print(abbr)
