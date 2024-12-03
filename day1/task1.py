f = open('input1.txt')

lines = f.readlines()

list=[]
for line in lines:
    list.extend(line.split())
    
    

list1 = []
list2 = []

for line in lines:
    numbers = line.strip().split() #die zwei zahlen aus einer zeile #strip leerzeichen am anfang und ende entfernen und split nach leerzeichen trennen
    list1.append(int(numbers[0]))  # Erste Zahl hinzufügen (als Ganzzahl)
    list2.append(int(numbers[1]))  # Zweite Zahl hinzufügen (als Ganzzahl)
    
list1.sort()
print(list1)
list2.sort()
print(list2)
result = 0
for i in range(len(list1)):
   result = result + abs(int(list1[i])-int(list2[i]))


print(result)   