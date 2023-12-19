FILE_NAME = 'input.txt'

class Aplenty:

    def __init__(self):
        self.workflows = {}
        self.inputs = []
        with open(FILE_NAME) as f:
            fill_dictionary = True
            for line in f.readlines():
                if line == '\n':
                    fill_dictionary = False
                elif fill_dictionary:
                    workflow = line.split('{')[0]
                    instructions = line.split('{')[1]
                    instructions = instructions.split(',')
                    order = []

                    for instruction in instructions:
                        # Check if it's the last instruction
                        if '}' in instruction:
                            self.workflows[workflow]['else'] = instruction.replace('}', '').replace('\n', '')
                        else:
                            comparator = '<' if '<' in instruction else '>'
                            variable = instruction.split(comparator)[0]
                            value = instruction.split(comparator)[1].split(':')[0]
                            result = instruction.split(comparator)[1].split(':')[1]
                            order.append(variable)

                            if workflow not in self.workflows:
                                self.workflows[workflow] = {}
                            
                            if variable not in self.workflows[workflow]:
                                self.workflows[workflow][variable] = {}
                                self.workflows[workflow][variable]['comparator'] = []
                                self.workflows[workflow][variable]['value'] = []
                                self.workflows[workflow][variable]['result'] = []
                            
                            self.workflows[workflow][variable]['comparator'].append(comparator)
                            self.workflows[workflow][variable]['value'].append(value)
                            self.workflows[workflow][variable]['result'].append(result)
                    else:
                        self.workflows[workflow]['order'] = order
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
            order_index = 0
            x = input[0]
            m = input[1]
            a = input[2]
            s = input[3]
            x_index = 0
            m_index = 0
            a_index = 0
            s_index = 0

            while result != 'A' and result != 'R':
                if order_index >= len(self.workflows[result]['order']):
                    result = self.workflows[result]['else']
                    order_index = 0
                else:
                    var_to_check = self.workflows[result]['order'][order_index]
                    if var_to_check == 'x':
                        var = x
                        index = x_index
                    elif var_to_check == 'm':
                        var = m
                        index = m_index
                    elif var_to_check == 'a':
                        var = a
                        index = a_index
                    else:
                        var = s
                        index = s_index
                    
                    comparator = self.workflows[result][var_to_check]['comparator'][index]
                    value = self.workflows[result][var_to_check]['value'][index]
                    if eval(f'{var} {comparator} {value}'):
                        order_index = 0
                        x_index = 0
                        m_index = 0
                        a_index = 0
                        s_index = 0
                        result = self.workflows[result][var_to_check]['result'][order_index]
                    else:
                        order_index += 1
                        index += 1
            
            if result == 'A':
                total_accepts += x + m + a + s
        print(f'Total result = {total_accepts}')



if __name__ == '__main__':
    aplenty = Aplenty()
    aplenty.evaluate()
