FILE_NAME = 'input.txt'

# NOTE: PART 1 REMOVED TO MAKE ROOM FOR PART 2
class LensLibrary:
    def __init__(self):
        self.hashmap = {}
        with open(FILE_NAME) as f:
            for line in f.readlines():
                list_of_vals = line.split(',')
                for list in list_of_vals:
                    self.__hash(list)
        
        print(f'Focusing Power = {self.__calculate_focusing_power()}')



    def __hash(self, list_of_chars):
        hash_value = 0
        for index, character in enumerate(list_of_chars):
            if character == '-' or character == '=':
                break
            val = ord(character)
            hash_value += val
            hash_value = (hash_value*17) % 256
        
        if character == '=':
            focal_length = list_of_chars[index+1:]
            if hash_value in self.hashmap:
                for item in self.hashmap[hash_value]:
                    if list_of_chars[:index] == item[0]:
                        item[1] = focal_length
                        break
                else:
                    self.hashmap[hash_value].append([list_of_chars[:index], focal_length])
            else:
                self.hashmap[hash_value] = [[list_of_chars[:index], focal_length]]
        else:
            if hash_value in self.hashmap:
                for item in self.hashmap[hash_value]:
                    if list_of_chars[:index] == item[0]:
                        self.hashmap[hash_value].remove(item)
        

    def __calculate_focusing_power(self):
        focusing_power = 0
        for key, value in self.hashmap.items():
            for i in range(len(value)):
                focusing_power += (int(key)+1) * (i+1) * int(value[i][1])
        
        return focusing_power



if __name__ == '__main__':
    lens_library = LensLibrary()
