FILE_NAME = 'input.txt'

class CosmicExpansion:

    def __init__(self):
        self.galaxy_list = []
        with open(FILE_NAME) as f:
            for line in f.readlines():
                if '#' in line:
                    self.galaxy_list.append(list(line.replace('\n', '')))
                else:
                    self.galaxy_list.append(['x'] * (len(line)-1))
        
        # Check for extra columns
        for j in range(len(self.galaxy_list[0])):
            for i in range(len(self.galaxy_list)):
                if self.galaxy_list[i][j] == '#':
                    break
            else:
                # Append extra row
                for row in self.galaxy_list:
                    row[j] = 'x'
    

    def get_galaxy_path_sums(self):
        # First get a list of all the positions of galaxies
        path_sums = 0
        galaxy_positions = self.__get_galaxy_positions()
        
        for i in range(len(galaxy_positions)):
            for j in range(i+1, len(galaxy_positions)):
                distance_i = abs(galaxy_positions[i][0] - galaxy_positions[j][0])
                distance_j = abs(galaxy_positions[i][1] - galaxy_positions[j][1])
                path_sums += distance_i + distance_j
        

        print(f'Distance between galaxies: {path_sums}')
    

    def __get_galaxy_positions(self):
        galaxy_positions = []
        for i in range(len(self.galaxy_list)):
            for j in range(len(self.galaxy_list[i])):
                if self.galaxy_list[i][j] == '#':
                    galaxy_positions.append((i, j))
        
        return galaxy_positions


    def get_far_galaxy_paths(self, empty_space_distance):
        path_sums = 0
        galaxy_positions = self.__get_galaxy_positions()
        
        for i in range(len(galaxy_positions)):
            for j in range(i+1, len(galaxy_positions)):
                total_distance = 0

                for x in range(min(galaxy_positions[i][0], galaxy_positions[j][0]), max(galaxy_positions[i][0], galaxy_positions[j][0])):
                    if self.galaxy_list[x][galaxy_positions[j][1]] == 'x':
                        total_distance += empty_space_distance
                    else:
                        total_distance += 1

                for x in range(min(galaxy_positions[i][1], galaxy_positions[j][1]), max(galaxy_positions[i][1], galaxy_positions[j][1])):
                    if self.galaxy_list[galaxy_positions[i][0]][x] == 'x':
                        total_distance += empty_space_distance
                    else:
                        total_distance += 1
                
                path_sums += total_distance

        print(f'Distance between galaxies with a space of {empty_space_distance}: {path_sums}')
    

    def __get_empty_spaces(self, pos_1, pos_2):
        # Go between the rows and colums and for each 'x' found, return +1
        empty_spaces_found = 0

        # Check for 'x' values in between rows
        for i in range(min(pos_1[0], pos_2[0]), max(pos_1[0], pos_2[0])):
            if self.galaxy_list[i][pos_1[1]] == 'x':
                empty_spaces_found += 1
        
        for j in range(min(pos_1[1], pos_2[1]), max(pos_1[1], pos_2[1])):
            if self.galaxy_list[pos_1[0]][j] == 'x':
                empty_spaces_found += 1
        
        return empty_spaces_found


if __name__ == '__main__':
    cosmic_expansion = CosmicExpansion()
    # cosmic_expansion.get_galaxy_path_sums()
    cosmic_expansion.get_far_galaxy_paths(2)
    cosmic_expansion.get_far_galaxy_paths(10)
    cosmic_expansion.get_far_galaxy_paths(100)
    cosmic_expansion.get_far_galaxy_paths(1000000)
