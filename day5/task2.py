
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
                return True
    return False

def sort_arr(result_arr, rules):
    sorted_update = update[:]
    changed = True
    while changed: 
        changed = False
        for rule in rules:
            before, after = rule
            if before in sorted_update and after in sorted_update:
                if sorted_update.index(before) > sorted_update.index(after):
                    idx_before = sorted_update.index(before) 
                    idx_after = sorted_update.index(after) 
                    temp = sorted_update[idx_before] 
                    sorted_update[idx_before] = sorted_update[idx_after] 
                    sorted_update[idx_after] = temp
                    changed = True
    return sorted_update
 
                


corrected_updates = []
for update in updates:
    if test(update, rules):  # Nur falsch sortierte Updates sortieren
        corrected_updates.append(sort_arr(update, rules))


print(corrected_updates)        
result = 0
for arr in corrected_updates:
    result = result + arr[len(arr) // 2]         


print(result)    
         