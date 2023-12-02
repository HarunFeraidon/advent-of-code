import sys
import re

def part1(input: str) -> int:
    lines = input.splitlines()
    r, g, b = 12, 13, 14
    total = 0
    for line in lines:
        game_info = line.split(':')
        game_id = int(game_info[0].split(" ")[1]) 
        skip = False
        
        for section in line.split(';'):
            colors_map = { }
            colors = getColors(section)

            for match in colors:
                number, color = match
                colors_map[color] = int(number)

            if ('red' in colors_map and r < colors_map['red']) or ('green' in colors_map and g < colors_map['green']) or ('blue' in colors_map and b < colors_map['blue']):
                skip = True
                break
        
        if not skip:
            print(game_id)
            total += game_id
        
    return total

def part2(input: str) -> int:
    lines = input.splitlines()
    total = 0

    for line in lines:
        colors_map = { }

        for section in line.split(';'):
            colors = getColors(section)

            for match in colors:
                number, color = match
                colors_map[color] = max(int(number), colors_map[color]) if color in colors_map else int(number)
        
        power = 1
        for color in colors_map:
            power = power * colors_map[color]
        print(power)
        total += power
        
    return total


def getColors(s: str) -> list[int]:
    pattern = r'(\d+)\s+(red|green|blue)'
    colors = re.findall(pattern, s)
    return colors
            

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pass in input")
        sys.exit(1)
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        input = file.read().strip()
    
    # print(part1(input))
    print(part2(input))