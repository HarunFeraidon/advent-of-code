import sys

def part1(input: str) -> int:
    lines = input.splitlines()
    grid = []
    for line in lines:
        grid.append(list(line))
    return search(grid)

def search(grid: list[list[str]]) -> int:
    total = 0

    def check_adjacent(x: int, y: int) -> bool:
        dirX = [-1, 0, 1]
        dirY = [-1, 0, 1]

        for dx in dirX:
            for dy in dirY:
                if dx == 0 and dy == 0:
                    continue 
                new_x = (dx+x) 
                new_y = (dy+y)
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    c = grid[new_x][new_y]
                    if not c.isnumeric() and c != '.':
                        return True
        return False
    
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[0]):
            value = grid[i][j]
            if value.isnumeric():
                found_symbol = check_adjacent(i,j)
                number = int(value)
                offset = 1
                lookahead = j + offset
                while lookahead < len(grid[0]) and grid[i][lookahead].isnumeric():
                    number = number*10 + int(grid[i][lookahead])
                    if not found_symbol:
                        found_symbol = check_adjacent(i, lookahead)
                    offset += 1
                    lookahead = j + offset
                j = lookahead
                if found_symbol:
                    total += number
            else:
                j += 1
        i += 1
    return total

# incomplete, i misintrepreted the example in the problem.
def part2(input: str) -> int:
    lines = input.splitlines()
    grid = []
    for line in lines:
        grid.append(list(line))
    return search_gears(grid)

def search_gears(grid: list[list[str]]) -> int:

    total = 0

    def check_adjacent(x: int, y: int) -> bool:
        dirX = [-1, 0, 1]
        dirY = [-1, 0, 1]

        results = set()

        for dx in dirX:
            for dy in dirY:
                if dx == 0 and dy == 0:
                    continue 
                new_x = (dx+x) 
                new_y = (dy+y)
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    c = grid[new_x][new_y]
                    if c.isnumeric():
                        left, right = -1, 1
                        while 0 <= new_y + left:
                            if grid[new_x][new_y+left].isnumeric():
                                left -= 1
                            else:
                                break
                        left += 1
                        while new_y + right < len(grid):
                            if grid[new_x][new_y+right].isnumeric():
                                right += 1
                            else:
                                break
                        # right -= 1
                        sublist = grid[new_x][new_y+left:new_y+right]
                        number_string = ''.join(sublist) 
                        number = int(number_string)
                        # print(number)
                        results.add(number)
            return results

    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[0]):
            value = grid[i][j]
            if value == "*":
                good_gears = check_adjacent(i, j)
                if good_gears and len(good_gears) == 2:
                    # print(f"good_gears: {good_gears}")
                    ratio = 1
                    for good_gear in good_gears:
                        ratio *= good_gear
                    total += ratio
            j += 1
        i += 1
    
    return total
                


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("pass in the input file too")
        sys.exit(1)
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        input = file.read().strip()
    
    # print(part1(input))
    print(part2(input))