from copy import deepcopy
from collections import deque
FILE_NAME = 'input.txt'

class LavaductLagoon:
    
    def __init__(self):
        self.holes = []
        with open(FILE_NAME) as f:
            for line in f.readlines():
                values = line.split()
                direction = values[0]
                length = values[1]
                rgb = values[2].replace('(', '').replace(')', '')
                self.holes.append([direction, length, rgb])


    def dig_hole(self):
        # coordinates = self.__get_coordinates()
        coordinates = self.__get_coordinates_from_instructions()
        coordinates = self.__zero_coordinates(coordinates)

        max_length = max(coord[1] for coord in coordinates)
        max_height = max(coord[0] for coord in coordinates)
        
        hole = []
        hole_length = []
        for i in range(max_length+1):
            hole_length.append('.')
        
        for j in range(max_height+1):
            hole.append(deepcopy(hole_length))
        
        self.__dig(hole, coordinates)
    
    
    def __get_coordinates(self):
        current_position = [0, 0]
        coordinates = [deepcopy(current_position)]
        for hole in self.holes:
            direction = hole[0]
            length = int(hole[1])
            
            current_position = self.__get_new_coordinate(current_position, direction, length)
            coordinates.append(deepcopy(current_position))
    
        return coordinates
    
    
    def __get_coordinates_from_instructions(self):
        current_position = [0, 0]
        coordinates = [deepcopy(current_position)]
        for hole in self.holes:
            instruction = hole[2]
            
            direction = instruction[len(instruction)-1] # The last character is the direction we're going in
            length = instruction[1:len(instruction)-1]  # Strip the beginning ('#') and the end (the direction)
            length = int(length, 16)
            
            if direction == '0':
                direction = 'R'
            elif direction == '1':
                direction = 'D'
            elif direction == '2':
                direction = 'L'
            else:
                direction = 'U'
            
            current_position = self.__get_new_coordinate(current_position, direction, length)
            coordinates.append(deepcopy(current_position))
        
        return coordinates
    
    
    def __get_new_coordinate(self, current_position, direction, length):
        if direction == 'R':
            current_position[1] += length
        elif direction == 'L':
            current_position[1] -= length
        elif direction == 'U':
            current_position[0] -= length
        else:
            current_position[0] += length
        
        return current_position
    
    
    def __zero_coordinates(self, coordinates):
        min_length = min(coord[1] for coord in coordinates)
        min_height = min(coord[0] for coord in coordinates)
        
        if min_length > 0:
            min_length = 0
        
        if min_height > 0:
            min_height = 0
        
        for coordinate in coordinates:
            coordinate[0] += abs(min_height)
            coordinate[1] += abs(min_length)
        
        return coordinates
    
    
    def __dig(self, hole, coordinates):
        for index in range(len(coordinates)-1):
            # Check if it's moving in the x or y direction
            min_i = min(coordinates[index][0], coordinates[index+1][0])
            max_i = max(coordinates[index][0], coordinates[index+1][0])
            current_j = coordinates[index][1]
            for i in range(min_i, max_i+1):
                hole[i][current_j] = '#'
            
            min_j = min(coordinates[index][1], coordinates[index+1][1])
            max_j = max(coordinates[index][1], coordinates[index+1][1])
            current_i = coordinates[index][0]
            for j in range(min_j, max_j+1):
                hole[current_i][j] = '#'
        
        for i in range(len(hole)):
            string = ''
            for j in range(len(hole[i])):
                string += hole[i][j]
            print(f'{string}\n')
        
        filled_hole = self.__flood_fill(hole)
        area = self.__calculate_area(filled_hole)
        print(f'Area of hole = {area}')
    
    
    def __flood_fill(self, hole, starting_i=0, starting_j=0):
        self.__output_hole(hole)
        
        queue = deque()
        queue.append([starting_i, starting_j])
        hole[starting_j][starting_i] = 'X'
        
        checked_tiles = []
        
        index = 0
        while queue:
            currTile = queue.popleft()
            i = currTile[0]
            j = currTile[1]
            
            # If we've already checked this tile, then return
            if [i, j] in checked_tiles:
                continue
            
            # Check each adjacent pixel to see if we've hit the wall of the hole. Valid in filling in the outside if we did not
            if i < len(hole) - 1 and hole[i+1][j] != '#':
                hole[i+1][j] = 'X'
                queue.append([i+1, j])
            
            if i > 0 and hole[i-1][j] != '#':
                hole[i-1][j] = 'X'
                queue.append([i-1, j])
            
            if j < len(hole[i]) - 1 and hole[i][j+1] != '#':
                hole[i][j+1] = 'X'
                queue.append([i, j+1])
            
            if j > 0 and hole[i][j-1] != '#':
                hole[i][j-1] = 'X'
                queue.append([i, j-1])
            
            # if index % 1000 == 0:
            #     self.__output_hole(hole)
            # index += 1
            
            checked_tiles.append([i, j])

        return hole

    
    def __calculate_area(self, hole):
        area = 0
        for line in hole:
            area += sum(1 for valid_location in line if valid_location != 'X')
        
        return area
    
    
    def __output_hole(self, hole):
        with open('output.txt', 'w') as f:
            for line in hole:
                for char in line:
                    f.write(char)
                f.write('\n')


    # The correct and easy way, while the other way is more fun.
    def shoelace_theorem(self):
        coordinates_pt_1 = self.__get_coordinates()
        coordinates_pt_2 = self.__get_coordinates_from_instructions()

        area_pt_1 = self.__shoelace(coordinates_pt_1)
        area_pt_2 = self.__shoelace(coordinates_pt_2)

        print(f'Part 1 Area: {area_pt_1}')
        print(f'Part 2 Area: {area_pt_2}')


    def __shoelace(self, coordinates):
        area = 0
        perimeter = 0
        for i in range(len(coordinates)):
            n = (i+1)%len(coordinates)
            x1 = coordinates[i][1]
            y1 = coordinates[i][0]
            x2 = coordinates[n][1]
            y2 = coordinates[n][0]
            
            area += (x1 * y2) - (x2 * y1)
            perimeter += abs((y2 - y1) + (x2 - x1))
        
        shoelace_area = area / 2
        shoelace_area += perimeter//2 + 1
        return shoelace_area


if __name__ == '__main__':
    lavaduct_lagoon = LavaductLagoon()
    lavaduct_lagoon.shoelace_theorem()