# CONSTANTS

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def main():
    # summation_of_ids = 0
    power_of_cubes = 0
    with open('input1.txt') as f:
        for line in f.readlines():
            id, sets = break_up_game_into_sets(line)

            # if check_validity(sets):
            #     summation_of_ids += id

            power_of_cubes += multiply_min_cubes_needed(sets)
    
    # print(summation_of_ids)
    print(power_of_cubes)


def break_up_game_into_sets(game: str):
    game_info = game.split(' ')
    game_id = game_info[1]
    game_id = int(game_id.replace(':', ''))
    
    sets = []
    current_set = []
    for index in range(2, len(game_info)):
        if index%2 == 0:
            num = int(game_info[index])
            color, end_of_set = extract_color(game_info[index+1])
            current_set.append((num, color))
            if end_of_set:
                sets.append(current_set)
                current_set = []
    
    return game_id, sets


def extract_color(color_val: str):
    ''' Formats the color to be better used in data, returns the color and if this is the end of the set. '''
    if ',' in color_val:
        color = color_val.replace(',', '')
        return color, False
    else:
        color = color_val.replace(';', '')
        color = color.replace('\n', '')
        return color, True


def check_validity(sets):
    ''' Part 1 in Cube Conundrum '''

    for set in sets:
        for result in set:
            val = result[0]
            color = result[1]

            if color == 'red':
                comparative_value = MAX_RED
            elif color == 'blue':
                comparative_value = MAX_BLUE
            elif color == 'green':
                comparative_value = MAX_GREEN
            else:
                print("Error, differing color than expected!")
                comparative_value = 0

            if val > comparative_value:
                return False

    return True


def multiply_min_cubes_needed(sets):
    ''' Part 2 in Cube Conundrum '''
    
    min_red = 0
    min_blue = 0
    min_green = 0

    for set in sets:
        for result in set:
            val = result[0]
            color = result[1]

            if color == 'red' and val > min_red:
                min_red = val
            elif color == 'blue' and val > min_blue:
                min_blue = val
            elif color == 'green' and val > min_green:
                min_green = val
    
    return min_red * min_blue * min_green


if __name__ == '__main__':
    main()
