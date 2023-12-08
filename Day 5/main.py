import copy

FILENAME = 'input1.txt'
NUM_CONVERSIONS = 7

class LocationFinder:
    def __init__(self):
        with open(FILENAME) as f:
            self.__get_seeds_pt_2(f.readline())
            for i in range(NUM_CONVERSIONS):
                self.__get_map(f)
                self.__convert_pt_2()
            
            print(f'Locations: {self.values}')
            print(f'Minimum value: {min(self.values)[0]}')


    def __get_seeds(self, seeds_line: str):
        seeds = seeds_line.split()
        self.values = seeds[1:]
    

    def __get_seeds_pt_2(self, seeds_line: str):
        seeds = seeds_line.split()
        seeds = seeds[1:]

        self.values = []
        for i in range(0, len(seeds), 2):
            self.values.append((int(seeds[i]), int(seeds[i]) + int(seeds[i+1])))


    def __get_map(self, f):
        self.source = []
        self.destination = []

        # Clear blank line
        f.readline()

        line_read = f.readline()
        while line_read != '\n':
            # This will be found at the end of the file
            if line_read == '':
                return
            
            if 'map' in line_read:
                line_read = f.readline()
                continue

            data = line_read.split()
            dest = int(data[0])
            source = int(data[1])
            rnge = int(data[2])
            
            self.source.append((source, source+rnge-1))
            self.destination.append((dest, dest+rnge-1))
            
            line_read = f.readline()
        
        combined_lists = list(zip(self.source, self.destination))
        map_list = sorted(combined_lists, key=lambda x: x[0])
        self.source, self.destination = zip(*map_list)


    def __convert(self):
        for i in range(len(self.values)):
            for index in range(len(self.source)):
                min_val = self.source[index][0]
                max_val = self.source[index][1]

                if int(self.values[i]) >= min_val and int(self.values[i]) <= max_val:
                    difference = int(self.values[i])-min_val
                    self.values[i] = self.destination[index][0]+difference
                    break
    

    def __convert_pt_2(self):
        old_list = copy.deepcopy(self.values)
        new_list = []
        for value in self.values:
            min_val = value[0]
            max_val = value[1]
            for j in range(len(self.source)):
                source = self.source[j]
                destination = self.destination[j]
                min_source = self.source[j][0]
                max_source = self.source[j][1]

                if min_val < min_source and max_val < min_source:
                    new_list.append((min_val, max_val))
                    break
                elif min_val < min_source and max_val <= max_source:
                    new_list.append((min_val, min_source-1))
                    new_list.append((self.destination[j][0], self.destination[j][1] - (max_source - max_val)))
                    break
                elif min_val < min_source and max_val > max_source:
                    new_list.append((min_val, min_source-1))
                    new_list.append((self.destination[j][0], self.destination[j][1]))
                    min_val = max_source+1
                
                if min_val >= min_source and max_val <= max_source:
                    new_list.append((self.destination[j][0] + (min_val - min_source), self.destination[j][1] - (max_source - max_val)))
                    break
                elif min_val >= min_source and min_val < max_source and max_val > max_source:
                    new_list.append((self.destination[j][0] + (min_val - min_source), self.destination[j][1]))
                    min_val = max_source + 1
            else:
                new_list.append((min_val, max_val))
        
        self.values = new_list
    

if __name__ == '__main__':
    LocationFinder()
