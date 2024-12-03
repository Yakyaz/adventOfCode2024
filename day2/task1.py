
f = open('input.txt')

lines = f.readlines()

listWithArrays = []


for line in lines:
    numbers = line.strip().split()  
    listWithArrays.append([int(num) for num in numbers])  # Konvertiere jedes Element zu int

counterResult = 0  #safe Arrays

for arr in listWithArrays:
    safe = True  
    if arr[0] < arr[1] and (arr[0] - arr[1]) <= 3:  
        max = arr[0]  
        for num in arr[1:]:
            if num > max and (num - max) <= 3:
                max = num
            else:
                safe = False
                break
    elif arr[0] > arr[1] and (arr[0] - arr[1]) <= 3:  
        min = arr[0]  
        for num in arr[1:]:
            if num < min and (min - num) <= 3:
                min = num
            else:
                safe = False
                break
    else:
        safe = False  

  
    if safe:
        counterResult += 1

print(counterResult)
