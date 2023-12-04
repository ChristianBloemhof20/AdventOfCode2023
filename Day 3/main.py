
def main():
    input = []
    with open('input1.txt') as f:
        for line in f.readlines():
            input.append(line)
    
    check_for_adjacent_parts(input)
    find_gear_ratio(input)



def check_for_adjacent_parts(input):
    '''
    We are going to parse through every value in the table, checking all possible adjacencies. If
    a number is adjacent to a symbol (up, down, or diagnal) then we're going to count it and add it.
    '''
    
    number_valid = False
    sum = 0
    current_number = ''

    # Parse through every value in the table
    for i in range(len(input)):
        for j in range(len(input[i])):
            # If we are on a non-digit, we don't care about adjacency. Reset the bool and continue
            if input[i][j].isdigit() == False:
                if number_valid == True:
                    sum += int(current_number)
                number_valid = False
                current_number = ''
            
            # To get to this elif statement, we know that it's a digit. If the number hasn't been confirmed, we're going to want to check it.
            elif number_valid == False:
                if check_valid_part_number(i, j, input):
                    number_valid = True
            
            if input[i][j].isdigit() == True:
                current_number += str(input[i][j])
    
    print('Sum from problem = ' + str(sum))



def check_valid_part_number(i, j, input):
    ''' Returns True if a symbol that is not a . is found around the number we're checking'''
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x >= 0 and x < len(input) and y >= 0 and y < len(input[i]) and not input[x][y].isalnum() and input[x][y] != '.' and input[x][y] != '\n':
                return True


def find_gear_ratio(input):
    ''' 
    Part 2 of Gear Ratios 
    Do the same thing as part 1, but for the asterisks instead (multiplying numbers... blah blah blah)
    '''

    gear_ratio = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '*':
                gear_ratio += get_gear_ratio(i, j, input)
    
    print(f'Gear Ratio Sum: {gear_ratio}')


def get_gear_ratio(i, j, input):
    numbers = []
    
    for x in range(i-1, i+2):
        found_num = False
        for y in range(j-1, j+2):
            if input[x][y].isdigit() and found_num == False:
                numbers.append(get_number(x, y, input))
                found_num = True
            elif found_num == True and input[x][y].isdigit() == False:
                found_num = False
    
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    
    return 0


def get_number(i, j, input):
    # Find the beginning of the number, trace it all the way to the end
    while (j-1 > -1 and input[i][j-1].isdigit() == True):
        j -= 1
    
    # Now we have the beginning of the number, trace it until we have the whole number collected
    num = ''
    while (input[i][j].isdigit() == True):
        num += input[i][j]
        j += 1
    
    return int(num)


if __name__ == '__main__':
    main()
