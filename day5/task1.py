
f = open('input.txt')

lines = f.readlines()

rules = []
updates = []
flag = False

for line in lines:
    line = line.strip() 
    if not line:  
        flag = True
        continue
    
    if not flag:
        rules.append(list(map(int, line.split('|')))) #Jede Zeile wird durch split('|') getrennt
    else:
        updates.append(list(map(int, line.split(','))))


def test(update, rules):
    for rule in rules:
        before, after = rule
        if before in update and after in update:
            if update.index(before) > update.index(after):
                return False 
    return True

result_arr = []

       
for update in updates:
    if test(update, rules):
        result_arr.append(update)  
        
result = 0
for arr in result_arr:
    result = result + arr[len(arr) // 2]         


print(result)    
         