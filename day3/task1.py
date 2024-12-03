import re

patternMul = r"(mul\(\d{1,3},\d{1,3}\))" #regex fuer mul(x,y) x,y Element von 1-3 stelligen zahlen

# Alle Treffer als Liste
matches = re.findall(patternMul, open('input.txt').read())

print(matches)

patternVal = r"mul\((\d+),(\d+)\)"

values = []
result = 0
#matches = 'mul(552,996)', 'mul(252,989)', 'mul(193,149)' 
for match in matches: #ich habe mein matches array nehme einen eintrag raus mul(552,996)
    tupelNum = re.findall(patternVal, match) # dann filtere ich das tupel raus (552,996)
    x, y = map(int, tupelNum[0])   # dann nehme ich das einzige tupel in meiner list tupelNum[0] und mappe durch die beiden x,y und mache sie jeweils zu int
    result = result + (x*y)
    

print(result)    