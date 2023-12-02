import sys

def part1(input: str) -> int:
    all_calibrations = get_numbers_list(input)
    print(all_calibrations)
    return sum(all_calibrations)

def get_numbers_list(input_str: str) -> list[int]:
    numbers = []
    lines = input_str.splitlines()
    for line in lines:
        left = 0
        right = len(line) - 1
        current = 0

        while left < len(line):
            if line[left].isdigit():
                current = int(line[left])
                break
            left += 1

        while right >= 0:
            if line[right].isdigit():
                current = current*10 + int(line[right])
                break
            right -= 1
        
        numbers.append(current)
    return numbers

def part2(input_str: str) -> int:
    lines = input_str.splitlines()
    first_num = None
    second_num = None
    total = 0
    for line in lines:
        first_num = find_first_num(line)
        second_num = find_second_num(line)
        total += first_num * 10 + second_num
    return total
        
def find_first_num(s: str) -> int:
    i=0
    while i < len(s):
        if s[i].isnumeric():
            return int(s[i])
        if s[i: i+3] == 'one':
            return 1
        if s[i: i+3] == 'two':
            return 2
        if s[i: i+5] == 'three':
            return 3 
        if s[i: i+4] == 'four':
            return 4
        if s[i: i+4] == 'five':
            return 5
        if s[i: i+3] == 'six':
            return 6
        if s[i: i+5] == 'seven':
            return 7
        if s[i: i+5] == 'eight':
            return 8
        if s[i: i+4] == 'nine':
            return 9
        i += 1

def find_second_num(s: str) -> int:
    i = len(s) - 1
    while i >= 0:
        if s[i].isnumeric():
            return int(s[i])
        if s[i-2: i+1] == 'one':
            return 1
        if s[i-2: i+1] == 'two':
            return 2
        if s[i-4: i+1] == 'three':
            return 3 
        if s[i-3: i+1] == 'four':
            return 4
        if s[i-3: i+1] == 'five':
            return 5
        if s[i-2: i+1] == 'six':
            return 6
        if s[i-4: i+1] == 'seven':
            return 7
        if s[i-4: i+1] == 'eight':
            return 8
        if s[i-3: i+1] == 'nine':
            return 9
        i -= 1

    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("pass in the input file too")
        sys.exit(1)
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        input = file.read().strip()
    
    # print(part1(input))
    print(part2(input))