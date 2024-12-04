f = open('input.txt')

lines = f.readlines()


rows = len(lines[0].strip()) 
cols = len(lines)


# 2D-Matrix erstellen
grid = []

for line in lines:
    grid.append(list(line.strip()))


directions = [
    (0, 1),  # nach rechts
    (0, -1), # nach links
    (1, 0),  # nach unten
    (-1, 0), # nach oben
    (1, 1),  # diagonal nach unten rechts
    (-1, -1), # diagonal nach oben links
    (1, -1), # diagonal nach unten links
    (-1, 1)  # diagonal nach oben rechts
]

word = "XMAS"
# Funktion, um XMAS zu prüfen
def check_xmas(grid, x, y, dx, dy):
    for char in range(len(word)):
        nx, ny = x + char*dx, y + char*dy #x=4+0*1 y=1+0*1
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[char]:
            return False
    return True
            
            
count = 0            
for x in range(rows):
    for y in range(cols):
        for dx, dy in directions:
            if check_xmas(grid, x, y, dx, dy):
                count += 1
                
                
print(count)                