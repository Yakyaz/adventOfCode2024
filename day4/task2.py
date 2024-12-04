f = open('input.txt')

lines = f.readlines()


rows = len(lines[0].strip()) 
cols = len(lines)


# 2D-Matrix erstellen
grid = []

for line in lines:
    grid.append(list(line.strip()))



word = "MAS"

def check_xmas(grid, x, y):
    # Prüfen, ob wir innerhalb der Grenzen sind
    if x - 1 < 0 or x + 1 >= rows or y - 1 < 0 or y + 1 >= cols:
        return False

    diagonal1 = grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1]  # von oben links nach unten rechts
    diagonal2 = grid[x-1][y+1] + grid[x][y] + grid[x+1][y-1]  # von oben rechts nach unten links

    return (diagonal1 == "MAS" or diagonal1 == "SAM") and (diagonal2 == "MAS" or diagonal2 == "SAM")
            
count = 0            
for x in range(rows):
    for y in range(cols):
        if grid[x][y] == "A":
            if check_xmas(grid, x, y):
                count += 1
                
                
print(count)                