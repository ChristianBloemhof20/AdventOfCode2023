import numpy as np
FILE_NAME = 'input.txt'

class PointOfIncidence:
    def __init__(self):
        self.patterns = []
        with open(FILE_NAME) as f:
            pattern = []
            for line in f.readlines():
                if line == '\n':
                    self.patterns.append(pattern)
                    pattern = []
                else:
                    pattern.append(list(line.replace('\n', '')))
            else:
                self.patterns.append(pattern)


    def find_reflections(self, smudges=0):
        total_count = 0

        for pattern in self.patterns:
            reflection_index = self.__find_reflection(pattern, smudges)
            if reflection_index != -1:
                print(reflection_index+1)
                total_count += reflection_index+1
                continue

            rotated_data = np.rot90(pattern)
            reflection_index = self.__find_reflection(rotated_data, smudges)
            print(reflection_index+1)
            total_count += ((reflection_index+1) * 100)
        
        print(f'Total value found with {smudges} smudges: {total_count}')

        

    def __find_reflection(self, pattern, smudges=0):
        ''' 
        Try to find a spot in row 1 where the values match. Once found, see if they spread all the way out to the ends.
        Repeat this process for all rows to see if valid.
        '''

        for i in range(len(pattern[0])-1):
            errors = 0

            for j in range(len(pattern)):
                distance = 0
                while i+1+distance < len(pattern[j]) and i-distance >= 0:
                    if pattern[j][i-distance] != pattern[j][i+1+distance]:
                        errors += 1
                    
                    if errors > smudges:
                        break
                    distance += 1
                
                if i+1+distance < len(pattern[j]) and i-distance >= 0:
                    break
            else:
                if errors == smudges:
                    return i
        

        return -1



if __name__ == '__main__':
    point_of_incidence = PointOfIncidence()
    # point_of_incidence.find_reflections()
    point_of_incidence.find_reflections(smudges=1)
