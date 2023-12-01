import re

''' Trebuchet Problem '''
def main():
    value = 0
    with open('input2.txt') as f:
        for line in f.readlines():
            converted_line = convert_words_to_numbers(line)
            value += add_first_and_last_numbers_to_value(converted_line)
    
    print(value)


def add_first_and_last_numbers_to_value(input):
    ''' Part 1 of the Trebuchet Problem '''
    
    numbers = re.sub('\D', '', input)
    combined_number = int(f'{numbers[0]}{numbers[len(numbers)-1]}')
    return combined_number


def convert_words_to_numbers(input: str):
    ''' Part 2 of the Trebuchet Problem '''
    
    converted_input = ''
    for index in range(len(input)):
        if input[index].isdigit():
            converted_input += input[index]
        else:
            val = check_for_word_next_word(input[index:])
            if val != -1:
                converted_input += val
    
    return converted_input


def check_for_word_next_word(remaining_word):
    filtered_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    current_word = ''
    for letter in remaining_word:
        current_word += letter
        filtered_words = filter_words(current_word, filtered_words)
        if len(filtered_words) == 0:
            break

        success = check_for_word(current_word, filtered_words)
        if success:
            return convert_to_number(current_word)
    
    return -1
        

def filter_words(current_word, remaining_list):
    new_list = []
    for item in remaining_list:
        if current_word in item:
            new_list.append(item)
    
    return new_list


def check_for_word(current_word, remaining_list):
    for item in remaining_list:
        if current_word == item:
            return True


def convert_to_number(word: str):
    word = word.replace('one', '1')
    word = word.replace('two', '2')
    word = word.replace('three', '3')
    word = word.replace('four', '4')
    word = word.replace('five', '5')
    word = word.replace('six', '6')
    word = word.replace('seven', '7')
    word = word.replace('eight', '8')
    word = word.replace('nine', '9')

    return word


if __name__ == '__main__':
    main()
