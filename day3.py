if(input("test?\n") in ["1", "t", "y"]):
    lines = open("input_test.txt", "r")
else:
    lines = open("input.txt", "r")

grid = []# grid

for line in lines:
    line = line.strip()
    grid.append(line)

def get_parts(grid):
    number_parts = []
    numbers = "1,2,3,4,5,6,7,8,9,0".split(",")
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if(grid[y][x] in numbers):
                if(x == 0):
                    number_parts.append([x, y])
                elif(grid[y][x-1] not in numbers):
                    number_parts.append([x, y])
    return number_parts

def get_part_length(grid, part):
    numbers = "1,2,3,4,5,6,7,8,9,0".split(",")
    for x in range(part[0], len(grid[0])):
        if(grid[part[1]][x] not in numbers):
            x -= 1
            break
    return x - part[0] + 1

def neighbour_symbols(grid, pos):
    symbols = "!,@,#,$,%,^,&,*,(,),-,_,=,+,/,?,:,;,],},[,{,`,~,|,\\,\",\'".split(",")
    neighbours = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    for neighbour in neighbours:
        check_pos = (neighbour[0] + pos[0], neighbour[1] + pos[1])
        if(check_pos[0] < len(grid[0]) and check_pos[0] >= 0 and check_pos[1] < len(grid) and check_pos[1] >= 0):
            if(grid[check_pos[1]][check_pos[0]] in symbols):
                return True
    return False

def get_part_value(grid, part, part_length):
    result = 0
    for x in range(part_length):
        result += 10**(part_length-x-1) * int(grid[part[1]][part[0] + x])
    return result
    
def get_part_start(grid, pos):
    numbers = "1,2,3,4,5,6,7,8,9,0".split(",")
    for x in range(pos[0], -1, -1):
        if(grid[pos[1]][x] not in numbers):
            x += 1
            break
    return (x, pos[1])

def get_reverse_neighbours(grid, pos):
    result = []
    result_starts = []
    numbers = "1,2,3,4,5,6,7,8,9,0".split(",")
    neighbours = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    for neighbour in neighbours:
        check_pos = (neighbour[0] + pos[0], neighbour[1] + pos[1])
        if(check_pos[0] < len(grid[0]) and check_pos[0] >= 0 and check_pos[1] < len(grid) and check_pos[1] >= 0):
            if(grid[check_pos[1]][check_pos[0]] in numbers):
                if(get_part_start(grid, check_pos) not in result_starts):
                    result.append(check_pos)
                    result_starts.append(get_part_start(grid, check_pos))
    return result
    
def get_gears(grid):
    gears = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if(grid[y][x] == "*"):
                reverse_neighbours = get_reverse_neighbours(grid, (x, y))
                if(len(reverse_neighbours) == 2):
                    gears.append((x, y))
    return gears

def get_reverse_value(grid, pos):
    numbers = "1,2,3,4,5,6,7,8,9,0".split(",")
    for x in range(pos[0], -1, -1):
        if(grid[pos[1]][x] not in numbers):
            x += 1
            break
    part = (x, pos[1])
    part_length = get_part_length(grid, part)

    return get_part_value(grid, part, part_length)
    
# part 1
parts = get_parts(grid)
suma = 0

for part in parts:
    valid_part = False
    part_length = get_part_length(grid, part)
    for x in range(part[0], part[0] + part_length):
        if(neighbour_symbols(grid, (x, part[1]) )):
            valid_part = True
    
    if(valid_part):
        suma += get_part_value(grid, part, part_length)

print(suma)

suma = 0
# part 2
gears = get_gears(grid)
for gear in gears:
    temp = 1
    reverse_neighbours = get_reverse_neighbours(grid, (gear[0], gear[1]))
    for neighbour in reverse_neighbours:
        temp *= get_reverse_value(grid, neighbour)
    suma += temp
print(suma)
# 6719247886 too high
# 63881026 too low
            
