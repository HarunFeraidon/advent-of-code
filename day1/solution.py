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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("pass in the input file too")
        sys.exit(1)
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        input = file.read().strip()
    
    print(part1(input))