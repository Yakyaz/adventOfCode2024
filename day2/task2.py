f = open('input.txt')

lines = f.readlines()

listWithArrays = []


for line in lines:
    numbers = line.strip().split()  
    listWithArrays.append([int(num) for num in numbers])  # Konvertiere jedes Element zu int

def checkMonotonic3(arr):
    ascending = all(arr[i] < arr[i + 1] and 1 <= arr[i + 1] - arr[i] <= 3 for i in range(len(arr) - 1))
    descending = all(arr[i] > arr[i + 1] and 1 <= arr[i] - arr[i + 1] <= 3 for i in range(len(arr) - 1))
    return ascending or descending
    

def makeSafe(arr):
    for i in range(len(arr)):
        temp = arr[:i] + arr[i + 1:]  
        if checkMonotonic3(temp):
            return temp 

count = 0

for arr in listWithArrays:
    if checkMonotonic3(arr):
        count += 1  
    else:
        testArr = makeSafe(arr)
        if testArr:  # in Python werden nicht leere arrays als True gesehen
            count += 1
print(count)





