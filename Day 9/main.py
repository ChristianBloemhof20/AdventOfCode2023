FILE_NAME = 'input.txt'

class MirageMaintenance:
    def __init__(self):
        next_total = 0
        prev_total = 0
        with open(FILE_NAME) as f:
            for line in f.readlines():
                if line != '\n':
                    next_total_increment, prev_total_increment = self.__calculate_series(line)
                    next_total += next_total_increment
                    prev_total += prev_total_increment
        
        print(f'Next Total Value: {next_total}')
        print(f'Previous Total Value: {prev_total}')
    
    def __calculate_series(self, line: str):
        sequences = []
        current_sequence = line.split()
        current_sequence = [int(x) for x in current_sequence]
        sequences.append(current_sequence)
        
        while sum(current_sequence) != 0:
            prev_sequence = current_sequence
            current_sequence = []
            for i in range(len(prev_sequence)-1):
                current_sequence.append(prev_sequence[i+1] - prev_sequence[i])
            
            sequences.append(current_sequence)
        
        next_in_sequence = self.__calculate_next_in_series(sequences)
        prev_in_sequence = self.__calculate_previous_in_series(sequences)
        
        return next_in_sequence[0][len(next_in_sequence[0])-1], prev_in_sequence[0][0]

    
    def __calculate_next_in_series(self, sequences: list):
        sequences[len(sequences)-1].append(0)
        for i in range(len(sequences)-1, 0, -1):
            new_value = sequences[i][len(sequences[i])-1] + sequences[i-1][len(sequences[i])-1]
            sequences[i-1].append(new_value)
        
        return sequences
    
    
    def __calculate_previous_in_series(self, sequences: list):
        sequences[len(sequences)-1].insert(0, 0)
        for i in range(len(sequences)-1, 0, -1):
            new_value = sequences[i-1][0] - sequences[i][0]
            sequences[i-1].insert(0, new_value)
        
        return sequences


if __name__ == '__main__':
    mirage_maintenance = MirageMaintenance()
