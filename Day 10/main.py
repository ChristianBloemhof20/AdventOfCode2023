FILE_NAME = 'test5.txt'

class PipeMaze:
    def __init__(self):
        self.maze = []
        with open(FILE_NAME) as f:
            for line in f.readlines():
                if line != '\n':
                    self.maze.append(list(line))
        
        self.__find_starting_position()
    
    
    def __find_starting_position(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'S':
                    self.starting_i = i
                    self.starting_j = j
                    return
    
    
    def find_furthest_location(self):
        locations = []
        i, j, direction = self.__check_around_start(self.starting_i, self.starting_j)
        locations.append((i, j))
        
        current_tile = self.maze[i][j]
        while current_tile != 'S':
            locations.append((i, j))
            if direction == 'W':
                direction_approached = 'E'
            elif direction == 'E':
                direction_approached = 'W'
            elif direction == 'N':
                direction_approached = 'S'
            else:
                direction_approached = 'N'
            self.maze[i][j] = direction_approached
            i, j, direction = self.__get_next_location(current_tile, i, j, direction)
            current_tile = self.maze[i][j]
        
        mid_point = len(locations)//2
        print(f'Mid Point = {mid_point}')
        
        self.path_tiles = locations
    
    
    def __check_around_start(self, i, j):
        ''' Check the 4 directions around the start to see which way to begin going. '''
        
        if i-1 > 0 and self.maze[i-1][j] !='.' and self.maze[i-1][j] != '-' and self.maze[i-1][j] != 'L' and self.maze[i-1][j] != 'J' :
            return i-1, j, 'S'
        elif j-1 > 0 and self.maze[i][j-1] != '.' and self.maze[i][j-1] != '|' and self.maze[i][j-1] != 'J' and self.maze[i][j-1] != '7':
            return i, j-1, 'E'
        elif j+1 < len(self.maze[i]) and self.maze[i][j+1] != '.' and self.maze[i][j+1] != '|' and self.maze[i][j+1] != 'F' and self.maze[i][j+1] != 'L':
            return i, j+1, 'W'
        else:
            return i+1, j, 'N'
    
    
    def __get_next_location(self, tile, i, j, entry_direction):
        if tile == '|':
            if entry_direction == 'N':
                return i+1, j, 'N'
            else:
                return i-1, j, 'S'
        elif tile == '-':
            if entry_direction == 'W':
                return i, j+1, 'W'
            else:
                return i, j-1, 'E'
        elif tile == 'L':
            if entry_direction == 'N':
                return i, j+1, 'W'
            else:
                return i-1, j, 'S'
        elif tile == 'J':
            if entry_direction == 'N':
                return i, j-1, 'E'
            else:
                return i-1, j, 'S'
        elif tile == '7':
            if entry_direction == 'W':
                return i+1, j, 'N'
            else:
                return i, j-1, 'E'
        elif tile == 'F':
            if entry_direction == 'E':
                return i+1, j, 'N'
            else:
                return i, j+1, 'W'
        else:
            print('ERROR: TILE NOT VALID')
    
    
    def count_inside_tiles(self):
        tiles_in_loop = 0
        self.s_val = self.__get_start_directions()
        skip = ''
        
        for i in range(len(self.maze)):
            inside_loop = False
            for j in range(len(self.maze[i])):
                tile = self.maze[i][j]
                if tile == 'S':
                    tile = self.s_val
                
                if (i, j) in self.path_tiles:
                    if tile == 'N':
                        inside_loop = True
                    elif tile == 'S':
                        inside_loop = False
                elif inside_loop:
                    tiles_in_loop += 1
        
        print(tiles_in_loop)
    
    
    def __get_start_directions(self):
        i = self.starting_i
        j = self.starting_j
        
        if i-1 > 0 and self.__valid_north(self.maze[i-1][j]):
            if j-1 > 0 and self.__valid_west(self.maze[i][j-1]):
                return 'J'
            elif j+1 < len(self.maze[i]) and self.__valid_east(self.maze[i][j+1]):
                return 'L'
            else:
                return '|'
        elif j-1 > 0 and self.__valid_west(self.maze[i][j-1]):
            # North not valid
            if j+1 < len(self.maze[i]) and self.__valid_east(self.maze[i][j+1]):
                return '-'
            else:
                return '7'
        else:
            return 'F'
    
    
    def __valid_north(self, tile):
        if tile != '.' and tile != '-' and tile != 'L' and tile != 'J':
            return True
        return False

    
    def __valid_south(self, tile):
        if tile != '.' and tile != '-' and tile != '7' and tile != 'F':
            return True
        return False
    
    
    def __valid_east(self, tile):
        if tile != '.' and tile != '|' and tile != 'F' and tile != 'L':
            return True
        return False
    
    
    def __valid_west(self, tile):
        if tile != '.' and tile != '|' and tile != 'J' and tile != '7':
            return True
        return False


if __name__ == '__main__':
    pipe_maze = PipeMaze()
    pipe_maze.find_furthest_location()
    pipe_maze.count_inside_tiles()
