import sys

def part1(input: str) -> int:
    lines = input.splitlines()
    total = 0
    for line in lines:
        game_info = line.split(':')[1]
        card1, card2 = game_info.split('|')
        winnings = set([ int(x) for x in card1.split() ])
        my_numbers = set([ int(x) for x in card2.split() ])
    
        points = 0
        for winner in winnings:
            if winner in my_numbers:
                points = points * 2 if points != 0 else 1
        total += points
    return total


def part2(input: str) -> int:
    lines = input.splitlines()
    points_per_card = []
    total = 0

    for line in lines:
        game_info = line.split(':')[1]
        card1, card2 = game_info.split('|')
        winnings = set([ int(x) for x in card1.split() ])
        my_numbers = set([ int(x) for x in card2.split() ])

        counter = 0
        for winner in winnings:
            if winner in my_numbers:
                counter += 1
        points_per_card.append(counter)
    
    card_copies = [1] * len(points_per_card)

    i = 0
    while i < len(card_copies):
        points = points_per_card[i]
        curr_copies = card_copies[i]
        for _ in range(curr_copies):
            for k in range(1, points+1):
                card_copies[i+k] += 1

        i += 1

    print(card_copies)
    total = sum(card_copies)

    return total



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pass in input")
        sys.exit(1)
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        input = file.read().strip()
    
    # print(part1(input))
    print(part2(input))