FILE_NAME = 'test.txt'

from functools import cache

class Aplenty:

    def __init__(self):
        self.workflows = {}
        self.inputs = []
        
        self.ranges = {}
        self.ranges['x'] = [0, 4000]
        self.ranges['m'] = [0, 4000]
        self.ranges['a'] = [0, 4000]
        self.ranges['s'] = [0, 4000]
        
        with open(FILE_NAME) as f:
            fill_dictionary = True
            for line in f.readlines():
                if line == '\n':
                    fill_dictionary = False
                elif fill_dictionary:
                    workflow = line.split('{')[0]
                    instructions = line.split('{')[1]
                    instructions = instructions.split(',')

                    for instruction in instructions:
                        # Check if it's the last instruction
                        if '}' in instruction:
                            self.workflows[workflow]['else'] = instruction.replace('}', '').replace('\n', '')
                        else:
                            if workflow not in self.workflows:
                                self.workflows[workflow] = {}
                                self.workflows[workflow]['conditional'] = []
                            
                            self.workflows[workflow]['conditional'].append(instruction)
                else:
                    values = line.replace('{', '').replace('}', '')
                    values = values.split(',')
                    x = int(values[0].split('=')[1])
                    m = int(values[1].split('=')[1])
                    a = int(values[2].split('=')[1])
                    s = int(values[3].split('=')[1].replace('\n', ''))
                    self.inputs.append([x, m, a, s])

    def evaluate(self):
        total_accepts = 0
        for input in self.inputs:
            result = 'in'
            x = input[0]
            m = input[1]
            a = input[2]
            s = input[3]
            index = 0

            while result != 'A' and result != 'R':
                if index >= len(self.workflows[result]['conditional']):
                    result = self.workflows[result]['else']
                    index = 0
                else:
                    
                    conditional = self.workflows[result]['conditional'][index]
                    condition = conditional.split(':')[0]
                    condition_result = conditional.split(':')[1]
                    if 'x' in condition:
                        condition = condition.replace('x', str(x))
                    elif 'm' in condition:
                        condition = condition.replace('m', str(m))
                    elif 'a' in condition:
                        condition = condition.replace('a', str(a))
                    else:
                        condition = condition.replace('s', str(s))
                    
                    if eval(condition):
                        index = 0
                        result = condition_result
                    else:
                        index += 1
            
            if result == 'A':
                total_accepts += x + m + a + s
        return total_accepts

    @cache
    def find_all_possible_combinations(self, current_workflow='in'):
        # Find all possible paths to an A or an R and sum up the acceptance criteria to get there
        if current_workflow == 'A':
            return True
        elif current_workflow == 'R':
            return False
        else:
            conditions = self.workflows[current_workflow]['conditional']
            for condition in conditions:
                c, r = condition.split(':')
                res = self.find_all_possible_combinations(r)
                if res != False:
                    operator = '>' if '>' in c else '<'
                    var = c.split(operator)[0]
                    num = int(c.split(operator)[1])
                    if operator == '>':
                        self.ranges[var][0] = max(self.ranges[var][0], num+1)
                    else:
                        self.ranges[var][1] = min(self.ranges[var][1], num-1)
                else:
                    return False
            
            return True
    
    def calculate_combinations(self):
        x_val = self.ranges['x'][1] - self.ranges['x'][0]
        m_val = self.ranges['m'][1] - self.ranges['m'][0]
        a_val = self.ranges['a'][1] - self.ranges['a'][0]
        s_val = self.ranges['s'][1] - self.ranges['s'][0]
        print(f'Combinations: {x_val * m_val * a_val * s_val}')

    
if __name__ == '__main__':
    aplenty = Aplenty()
    total_accepts = aplenty.evaluate()
    print(f'Total result = {total_accepts}')
    
    combinational_accepts = aplenty.find_all_possible_combinations()
    aplenty.calculate_combinations()
    print(f'Total Combinational Results = {combinational_accepts}')
