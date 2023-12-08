from functools import reduce
from operator import mul
import math

FILENAME = 'input2.txt'

class WaitForIt:
    
    def __init__(self):
        self.__get_data()


    def __get_data(self):
        with open(FILENAME) as f:
            self.times = f.readline().split()[1:]
            self.distance = f.readline().split()[1:]
    

    def part_1(self):
        list_of_wins = []

        for i in range(len(self.times)):
            ways_to_win = 0
            for time_held in range(int(self.times[i])):
                # Formula: Distance = time held x time remaining
                distance_reached = time_held * (int(self.times[i]) - time_held)
                if distance_reached > int(self.distance[i]):
                    ways_to_win += 1
            
            list_of_wins.append(ways_to_win)
        
        print(f'Wins: {list_of_wins}')
        print(f'Final Result: {reduce(mul, list_of_wins)}')


    def quadratic_formula(self):
        pass


if __name__ == '__main__':
    day_6_problem = WaitForIt()
    day_6_problem.part_1()

