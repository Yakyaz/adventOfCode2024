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
directions = ["^", ">", "v", "<"]  
dx = [0, 1, 0, -1]  
dy = [-1, 0, 1, 0] 

current_direction = directions.index("^")

is_out = False
   
def simulate(grid, guard_x, guard_y):
    visited = set()  # Alle besuchten Positionen speichern ( weil der darf nur einmal eine besuchen, sonst loop)
    current_x, current_y = guard_x, guard_y
    current_dir = directions.index("^")
    
    while True:
        #wenn visited, dann loop    
        if (current_x, current_y, current_dir) in visited:
            return True
        visited.add((current_x, current_y, current_dir))
        
   
        next_x = current_x + dx[current_dir]
        next_y = current_y + dy[current_dir]

        if next_x < 0 or next_x >= cols or next_y < 0 or next_y >= rows:
            return False  
        

        if grid[next_y][next_x] == "#":
            # Hindernis -> Drehen im Uhrzeigersinn
            current_dir = (current_dir + 1) % 4
        else:
            # Vorwaerts bewegen
            current_x, current_y = next_x, next_y


# Zähle alle möglichen Hindernispos
valid_positions = 0

for y in range(rows):
    for x in range(cols):
        # Nur leere Felder (.) koenne hindernis sein
        if grid[y][x] == ".":
            # Temporaer ein Hindernis hinzufügen
            grid[y][x] = "#"
            
            if simulate(grid, guard_x, guard_y):
                valid_positions += 1
            # Hindernis entfernen
            grid[y][x] = "."

print(valid_positions)