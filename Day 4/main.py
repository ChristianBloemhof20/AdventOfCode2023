FILENAME = 'input1.txt'


def main():
    card_num = 1
    winning_number_score = 0

    with open(FILENAME) as f:
        line_count = sum(1 for line in f)
        card_number_list = [1] * line_count
        f.seek(0)

        for line in f.readlines():
            card_score, num_of_wins = check_winning_numbers(line)
            winning_number_score += card_score

            for i in range(card_num, card_num+num_of_wins):
                if i < len(card_number_list):
                    card_number_list[i] = card_number_list[i] + card_number_list[card_num-1] # Add 1 card per duplicate, so add the number of duplicate cards

            card_num += 1
    
    print(f'Score of winning numbers: {winning_number_score}')
    print(f'Total number of cards: {sum(card_number_list)}')



def check_winning_numbers(card: str):
    ''' Part 1 & Part 2 Combined '''

    numbers = card.split(':')[1]
    winning_numbers = numbers.split('|')[0].split()
    your_numbers = numbers.split('|')[1].split()

    number_of_wins = 0
    for number in winning_numbers:
        if number in your_numbers:
            number_of_wins += 1
    
    if number_of_wins > 0:
        score = 2**(number_of_wins-1)
    else:
        score = 0
    
    return score, number_of_wins



if __name__ == '__main__':
    main()
