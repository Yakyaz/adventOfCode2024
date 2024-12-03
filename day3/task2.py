import re

content = open('input.txt').read()

patterns = [
    r"(mul\(\d{1,3},\d{1,3}\))",
    r"do\(\)",
    r"don't\(\)"
    
]

compiled_patterns = [re.compile(pattern) for pattern in patterns] # in Regex-Objekte umgewandelt


matches = []
for pattern in compiled_patterns:
    matches.extend(pattern.finditer(content)) # gibt einen Iterator von Match-Objekten zurück


matches_sorted = sorted(matches, key=lambda match: match.start()) # Sortiere Treffer nach der Position im Text 

# Ausgabe der Treffer
matches_text = [match.group() for match in matches_sorted]

values = []
result = 0
flag = True
pattern_dont = r"don't\(\)"
pattern_do = r"do\(\)"
pattern_val = r"mul\((\d+),(\d+)\)"

for match in matches_text: 
    
    if(re.findall(pattern_dont, match)):
        flag = False
    
    if(re.findall(pattern_do, match)):
        flag = True
    
    if(flag):
        tupelNum = re.findall(pattern_val, match) 
        if tupelNum: 
            x, y = map(int, tupelNum[0])  
            result = result + (x*y)

print(result)    