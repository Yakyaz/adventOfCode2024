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

counter = 0    
result = 0
for num1 in list1:
    for num2 in list2:
        if(num1 == num2):
            counter = counter + 1
            
    result = result + (counter*num1)
    counter = 0
    
    
print(result)   