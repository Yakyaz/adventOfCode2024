input = open("input.txt")

lines = input.readlines()



lists = []
for line in lines:
    line = line.strip()
    key, values = line.split(':', 1)  # Teilt in zwei Teile
    # Speichere den Schlüssel und die Zahlen als eine Liste innerhalb einer Liste
    lists.append([int(key)] + list(map(int, values.strip().split())))


result = 0

def evaluate_all_combinations(numbers, current_result, index, key):
    if index == len(numbers):  
        return current_result == key

   
    if evaluate_all_combinations(numbers, current_result + numbers[index], index + 1, key):
        return True


    if evaluate_all_combinations(numbers, current_result * numbers[index], index + 1, key):
        return True
    
# Jede Liste prüfen
for lst in lists:
    key = lst[0] 
    numbers = lst[1:]  # Die Zahlen (Werte)
    if evaluate_all_combinations(numbers, numbers[0], 1, key):
        result += key


print(result)