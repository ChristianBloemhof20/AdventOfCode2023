from copy import deepcopy

FILE_NAME = 'input.txt'

class ReflectorDish:
    def __init__(self):
        self.dishes = []
        with open(FILE_NAME) as f:
            for line in f.readlines():
                self.dishes.append(list(line.replace('\n', '')))
    
    def move_north(self):
        ''' Go item by item seeing if we can move it north at all. When moving north, go until hit an item stopping. Start in the north. '''
        
        for i in range(1, len(self.dishes)):
            for j in range(len(self.dishes[i])):
                if self.dishes[i][j] == 'O':
                    rows_traveled = 1
                    while i-rows_traveled >= 0 and self.dishes[i-rows_traveled][j] != 'O' and self.dishes[i-rows_traveled][j] != '#':
                        self.dishes[i-rows_traveled][j] = 'O'
                        self.dishes[i-rows_traveled+1][j] = '.'
                        rows_traveled += 1
    

    def move_south(self):
        for i in range(len(self.dishes)-1, -1, -1):
            for j in range(len(self.dishes[i])):
                if self.dishes[i][j] == 'O':
                    rows_traveled = 1
                    while i+rows_traveled < len(self.dishes) and self.dishes[i+rows_traveled][j] != 'O' and self.dishes[i+rows_traveled][j] != '#':
                        self.dishes[i+rows_traveled][j] = 'O'
                        self.dishes[i+rows_traveled-1][j] = '.'
                        rows_traveled += 1


    def move_west(self):
        for row in self.dishes:
            for j in range(len(row)):
                if row[j] == 'O':
                    cols_traveled = 1
                    while j-cols_traveled >= 0 and row[j-cols_traveled] != 'O' and row[j-cols_traveled] != '#':
                        row[j-cols_traveled] = 'O'
                        row[j-cols_traveled+1] = '.'
                        cols_traveled += 1


    def move_east(self):
        for row in self.dishes:
            for j in range(len(row)-1, -1, -1):
                if row[j] == 'O':
                    cols_traveled = 1
                    while j+cols_traveled < len(row) and row[j+cols_traveled] != 'O' and row[j+cols_traveled] != '#':
                        row[j+cols_traveled] = 'O'
                        row[j+cols_traveled-1] = '.'
                        cols_traveled += 1


    def calculate_northern_load(self):
        ''' 
        Probably would be more optimal to just do this somehow in the movement function, but I think this is better separated
        for potential future use.
        '''

        northern_load = 0
        num_rows = len(self.dishes)
        
        for row in self.dishes:
            rock_count = row.count('O')
            northern_load += rock_count*num_rows
            num_rows -= 1
        
        return northern_load
    

    def move_cycles(self, num_cycles):
        cycles = {}

        flattened_tuple = tuple(item for sublist in self.dishes for item in sublist)
        cycles[hash(flattened_tuple)] = (deepcopy(self.dishes), 0, self.calculate_northern_load())
        for i in range(num_cycles):
            self.move_north()
            self.move_west()
            self.move_south()
            self.move_east()

            flattened_tuple = tuple(item for sublist in self.dishes for item in sublist)
            if hash(flattened_tuple) in cycles:
                # Looks complicated so let me explain. There is a start point, and a cycle start point.
                # Find the start point of the cycle
                index_of_start = cycles[hash(flattened_tuple)][1]
                cycles_remaining = num_cycles - i

                # The final index should be the modulus of the length of a cycle, added back to the index
                # of the start of the cycle (because now we're in cycle territory) and -1 because we are 0 indexed.
                final_index = (cycles_remaining % (len(cycles)-index_of_start)) + index_of_start - 1
                for key, value in cycles.items():
                    if value[1] == final_index:
                        self.dishes = value[0]
                        return
            else:
                cycles[hash(flattened_tuple)] = (deepcopy(self.dishes), i+1, self.calculate_northern_load())


    def __repr__(self) -> str:
        print_string = ''
        for row in self.dishes:
            for item in row:
                print_string += item
            print_string += '\n'
        
        return print_string



if __name__ == '__main__':
    reflector_dish = ReflectorDish()
    # reflector_dish.move_north()
    # print(reflector_dish)

    reflector_dish.move_cycles(1000000000)
    print(reflector_dish)
    print(f'Northern Load = {reflector_dish.calculate_northern_load()}')
