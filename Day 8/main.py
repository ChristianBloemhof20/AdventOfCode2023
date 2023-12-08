import math

FILE_NAME = 'input.txt'

class HauntedWasteland:
    def __init__(self):
        self.wasteland_map = {}
        with open(FILE_NAME) as f:
            travel_path = f.readline()
            self.travel_path = travel_path.replace('\n', '')
            
            for line in f.readlines():
                if line != '\n':
                    self.__create_node_map(line)
    
    
    def __create_node_map(self, line: str):
        location_vals = line.split()
        location = location_vals[0]
        left_location = location_vals[2][1:len(location_vals[2])-1]
        right_location = location_vals[3][:len(location_vals[3])-1]
        
        self.wasteland_map[location] = (left_location, right_location)
    
    
    def traverse_path(self, starting_location):
        current_location = starting_location
        
        locations_traveled = 0
        # MAKE SURE IS ZZZ IN PART 1, MAKE SURE ENDS WITH Z IN PART 2
        while current_location.endswith('Z') == False:
            direction = self.travel_path[locations_traveled%len(self.travel_path)]
            
            current_location = self.__traverse_location(current_location, direction)
            locations_traveled += 1
        
        print(f'Traveled to {locations_traveled} to reach destination')
        return locations_traveled
    
    
    def __traverse_location(self, current_location, direction):
        adjacent_locations = self.wasteland_map[current_location]
        if direction == 'L':
            current_location = adjacent_locations[0]
        else:
            current_location = adjacent_locations[1]
        
        return current_location
    
    
    def traverse_multiple_paths(self):
        current_locations = [key for key in self.wasteland_map if key.endswith('A')]
        starting_positions = []
        
        for location in current_locations:
            travel_time = self.traverse_path(location)
            starting_positions.append(travel_time)
        
        print(f'Locations traveled with multiple paths: {math.lcm(*starting_positions)}')


if __name__ == '__main__':
    haunted_wasteland = HauntedWasteland()
    haunted_wasteland.traverse_path('AAA')
    haunted_wasteland.traverse_multiple_paths()
