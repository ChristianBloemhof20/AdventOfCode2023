from copy import deepcopy
FILE_NAME = 'input.txt'

class LavaFloor:
    def __init__(self):
        self.grid = []
        with open(FILE_NAME) as f:
            for line in f.readlines():
                temp_list = []
                for char in line:
                    if char != '\n':
                        # On splitters, check if it has already been used to split in that direction. If so, then ignore
                        temp_list.append([char, []])
                self.grid.append(temp_list)
        
        self.untouched_grid = deepcopy(self.grid)


    def __repr__(self) -> str:
        print_string = ''
        for row in self.grid:
            for value in row:
                print_string += value
            print_string += '\n'
        
        return print_string[:len(print_string)-1]


    def find_largest_energizer(self):
        energizer_values = []
        for i in range(len(self.grid)):
            if i == 0 or i == len(self.grid)-1:
                for j in range(len(self.grid[i])):
                    if i == 0:
                        direction = 'D'
                    elif i == len(self.grid)-1:
                        direction = 'U'
                    elif j == 0:
                        direction = 'L'
                    else:
                        direction = 'R'
                    
                    energizer_values.append(self.trace_paths(i, j, direction))
            else:
                # Just check the 2 outside values
                energizer_values.append(self.trace_paths(i, 0, 'L'))
                energizer_values.append(self.trace_paths(i, len(self.grid[i])-1, 'R'))
        
        # Go through and check the 4 corners going outwards
        energizer_values.append(self.trace_paths(0, 0, 'L'))
        energizer_values.append(self.trace_paths(0, len(self.grid[i])-1, 'R'))
        energizer_values.append(self.trace_paths(len(self.grid)-1, 0, 'L'))
        energizer_values.append(self.trace_paths(len(self.grid)-1, len(self.grid[i])-1, 'R'))

        return max(energizer_values)



    def trace_paths(self, starting_i=0, starting_j=0, starting_direction='R'):
        self.grid = deepcopy(self.untouched_grid) # Make sure the grid is clean
        directions_to_go = [[starting_i, starting_j, starting_direction]]
        energized_value = 0

        while len(directions_to_go) > 0:
            direction_to_go = directions_to_go[0]
            directions_to_go.remove(direction_to_go)
            i = direction_to_go[0]
            j = direction_to_go[1]
            direction = direction_to_go[2]
            

            while i < len(self.grid) and i >= 0 and j < len(self.grid[i]) and j >= 0:
                tile = self.grid[i][j][0]
                directions_gone = self.grid[i][j][1]
                # If we haven't visited this location before, this is a new spot being energized
                if len(directions_gone) == 0:
                    energized_value += 1
                
                if tile == '|' and direction != 'U' and direction != 'D':
                    # If we've already been here, it's a loop. Break out of sequence
                    if len(directions_gone) > 0:
                        break

                    # Go up, set going down to be done later
                    i -= 1
                    direction = 'U'
                    directions_gone.append(['U', 'D'])
                    directions_to_go.append([i+1, j, 'D'])
                elif tile == '-' and direction != 'L' and direction != 'R':
                    # If we've already been here, it's a loop. Break out of sequence
                    if len(directions_gone) > 0:
                        break

                    # Go left, set going right to be done later
                    j -= 1
                    direction = 'L'
                    directions_gone.append(['L', 'R'])
                    directions_to_go.append([i, j+1, 'R'])
                elif tile == '/':
                    if direction == 'U':
                        if 'U' in directions_gone:
                            break

                        directions_gone.append('U')
                        j += 1
                        direction = 'R'
                    elif direction == 'D':
                        if 'D' in directions_gone:
                            break

                        directions_gone.append('D')
                        j -= 1
                        direction = 'L'
                    elif direction == 'L':
                        if 'L' in directions_gone:
                            break

                        directions_gone.append('L')
                        i += 1
                        direction = 'D'
                    else:
                        if 'R' in directions_gone:
                            break

                        directions_gone.append('R')
                        i -= 1
                        direction = 'U'
                elif tile == '\\':
                    if direction == 'U':
                        if 'U' in directions_gone:
                            break

                        directions_gone.append('U')
                        j -= 1
                        direction = 'L'
                    elif direction == 'D':
                        if 'D' in directions_gone:
                            break

                        directions_gone.append('D')
                        j += 1
                        direction = 'R'
                    elif direction == 'L':
                        if 'L' in directions_gone:
                            break

                        directions_gone.append('L')
                        i -= 1
                        direction = 'U'
                    else:
                        if 'R' in directions_gone:
                            break

                        directions_gone.append('R')
                        i += 1
                        direction = 'D'
                else:
                    # Continue in direction
                    directions_gone.append(direction)
                    i, j = self.__move_in_direction(direction, i, j)
        
        return energized_value



    # Too long for pythons stack size, had to switch :(
    def trace_paths_recursively(self, i=0, j=0, direction='R'):
        # Check if out of bounds
        if i > len(self.grid)-1 or i < 0 or j > len(self.grid[i])-1 or j < 0:
            return 0
        else:
            tile = self.grid[i][j][0]
            directions = self.grid[i][j][1]
            if len(directions) == 0:
                energize_val = 1
            else:
                energize_val = 0
            
            if tile == '|' and (direction == 'R' or direction == 'L'):
                # Check if we've already done this
                if 'U' in directions or 'D' in directions:
                    return 0
                
                # Calculate and return the paths in both directions
                directions.append('U')
                directions.append('D')
                paths = self.trace_paths(i-1, j, 'U') + energize_val
                return self.trace_paths(i+1, j, 'D') + paths
            elif tile == '-' and (direction == 'U' or direction == 'D'):
                # Check if we've already done this
                if directions == ['L', 'R']:
                    return 0
                
                # Same as above, just different directions
                directions.append('L')
                directions.append('R')
                paths = self.trace_paths(i, j+1, 'R') + energize_val
                return self.trace_paths(i, j-1, 'L') + paths
            elif tile == '/':
                if direction == 'L':
                    if 'D' in directions:
                        return 0
                    directions.append('D')
                    return self.trace_paths(i+1, j, 'D') + energize_val
                elif direction == 'R':
                    if 'U' in directions:
                        return 0
                    directions.append('U')
                    return self.trace_paths(i-1, j, 'U') + energize_val
                elif direction == 'U':
                    if 'U' in directions:
                        return 0
                    directions.append('R')
                    return self.trace_paths(i, j+1, 'R') + energize_val
                else:
                    if 'L' in directions:
                        return 0
                    directions.append('L')
                    return self.trace_paths(i, j-1, 'L') + energize_val
            elif tile == '\\':
                if direction == 'L':
                    if 'U' in directions:
                        return 0
                    directions.append('U')
                    return self.trace_paths(i-1, j, 'U') + energize_val
                elif direction == 'R':
                    if 'D' in directions:
                        return 0
                    directions.append('D')
                    return self.trace_paths(i+1, j, 'D') + energize_val
                elif direction == 'U':
                    if 'L' in directions:
                        return 0
                    directions.append('L')
                    return self.trace_paths(i, j-1, 'L') + energize_val
                else:
                    if 'U' in directions:
                        return 0
                    directions.append('R')
                    return self.trace_paths(i, j+1, 'R') + energize_val
            else:
                # This should happen if tile is a '.' or if it's a '-' or '|' but light is going in the wrong direction
                directions.append(direction)
                i, j = self.__move_in_direction(direction, i, j)
                return self.trace_paths(i, j, direction) + energize_val


    def __move_in_direction(self, direction, i, j):
        if direction == 'R':
            return i, j+1
        elif direction == 'L':
            return i, j-1
        elif direction == 'U':
            return i-1, j
        else:
            return i+1, j

if __name__ == '__main__':
    lava_floor = LavaFloor()
    tiles_covered = lava_floor.trace_paths()
    print(f'Energizer value for part 1: {tiles_covered}')

    max_energizer_value = lava_floor.find_largest_energizer()
    print(f'Maximum energy = {max_energizer_value}')