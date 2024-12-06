f = open('input.txt')

lines = f.readlines()


rows = len(lines[0].strip()) 
cols = len(lines)


# 2D-Matrix erstellen
grid = []

for line in lines:
    grid.append(list(line.strip()))

guard_x, guard_y = None, None

count = 0
for row in grid: 
    if "^" in row:  
        guard_x = row.index("^")  
        guard_y = count 
        break  
    count = count + 1   
   
   
   
#directions auf dx und dy angepasst ^ = (0,-1) sozusagen, also da geht der guard hin    
directions = ["^", ">", "v", "<"]  # Reihenfolge der Drehung (uhrzeiger)
dx = [0, 1, 0, -1]  
dy = [-1, 0, 1, 0] 

current_direction = directions.index("^")

is_out = False
   
while not is_out:

    grid[guard_y][guard_x] = "X"
    
    next_x = guard_x + dx[current_direction]
    next_y = guard_y + dy[current_direction]
    

    if next_x < 0 or next_x >= cols or next_y < 0 or next_y >= rows:
        is_out = True
        break

    
    if grid[next_y][next_x] == "#":
        # Drehen im Uhrzeigersinn
        current_direction = (current_direction + 1) % 4
    else:
         # Vorwaerts bewegen
        guard_x, guard_y = next_x, next_y


counter = 0
for row in grid:
   counter = counter + row.count("X")

print(counter)   