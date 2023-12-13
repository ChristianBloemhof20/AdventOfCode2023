import functools

FILE_NAME = 'test1.txt'

class HotSprings:
    def __init__(self, mult_val=1):
        self.count = 0
        with open(FILE_NAME) as f:
            for line in f.readlines():
                values = line.split()[0]
                values = '?'.join([values] * mult_val)

                springs = line.split()[1].split(',')
                springs = springs * mult_val

                val = self.__get_combinations(values, tuple(springs))
                self.count += val
                print(f'Found Value: {val}')
        
        print(f'Total Combinations: {self.count}')
    
    @functools.lru_cache
    def __get_combinations(self, values, springs, length_current_spring=0):
        # We get to the end and all springs are made
        if len(values) == 0:
            if len(springs) == 0:
                return 1
            return 0
        
        symbol = values[0]

        # If our current symbol is a #, then we've either completed the spring or we're building the spring larger
        if symbol == '#':
            if len(springs) == 0:
                return 0
            
            if length_current_spring+1 == int(springs[0]):
                # This is a completed spring. Pop the spring off the list and pass -1 to identify that the prev was a spring
                return self.__get_combinations(values[1:], springs[1:], -1)
            # If this is an invalid spring, return it
            elif length_current_spring == -1:
                return 0
            else:
                return self.__get_combinations(values[1:], springs, length_current_spring+1)
        # If our current symbol is a ., then we're in a space between.
        elif symbol == '.':
            if length_current_spring > 0:
                return 0
            else:
                return self.__get_combinations(values[1:], springs)
        # Our symbol has to be a ?, check if it is valid to place here
        else:
            val = 0

            # Ensure that the previous one wasn't a completed spring
            if length_current_spring != -1 and len(springs) > 0:
                # If it's a question mark and the last isn't a spring, try to make this one a spring
                if length_current_spring+1 == int(springs[0]):
                    val = self.__get_combinations(values[1:], springs[1:], -1)
                else:
                    val = self.__get_combinations(values[1:], springs, length_current_spring+1)
                
            # Check combinations for passing it as a .
            if length_current_spring > 0:
                return val
            else:
                return self.__get_combinations(values[1:], springs) + val




if __name__ == '__main__':
    # hot_springs = HotSprings()
    hot_springs_mult = HotSprings(5)
