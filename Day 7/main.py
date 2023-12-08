FILE_NAME = 'input.txt'

class CamelCards:
    def __init__(self):
        self.hands = []
        with open(FILE_NAME) as f:
            for line in f.readlines():
                self.hands.append(CamelCard(line.split()[0], int(line.split()[1])))

        sorted_hand = sorted(self.hands)
        winnings = self.__calculate_winnings(sorted_hand)
        print(f'Winnings: {winnings}')

    def __calculate_winnings(self, sorted_hand):
        winnings = 0
        for i in range(len(sorted_hand)):
            winnings += (sorted_hand[i].bid * (i+1))
        
        return winnings


class CamelCard:
    def __init__(self, cards: str, bid: int):
        self.bid = bid
        self.__convert_cards(cards)
        self.__calculate_strength()


    def __convert_cards(self, cards: str):
        self.cards = list(cards)
        for i in range(len(self.cards)):
            if self.cards[i] == 'A':
                self.cards[i] = 14
            elif self.cards[i] == 'K':
                self.cards[i] = 13
            elif self.cards[i] == 'Q':
                self.cards[i] = 12
            elif self.cards[i] == 'J':
                self.cards[i] = 1
            elif self.cards[i] == 'T':
                self.cards[i] = 10
            else:
                self.cards[i] = int(self.cards[i])


    def __calculate_strength(self):
        cards_by_suit = [0] * 13
        jokers = 0
        for val in self.cards:
            if val == 1:
                jokers += 1
            else:
                cards_by_suit[val-2] = cards_by_suit[val-2] + 1
        
        # Remove all 0s
        filtered_cards_by_suit = [x for x in cards_by_suit if x != 0]
        if len(filtered_cards_by_suit) > 0:
            max_val = max(filtered_cards_by_suit)
        else:
            max_val = 0
        
        if (max_val + jokers) == 5:
            self.strength = 7
        elif (max_val + jokers) == 4:
            self.strength = 6
        elif (max_val + jokers) == 3:
            if max_val == 3:
                if 2 in filtered_cards_by_suit or jokers == 1:
                    self.strength = 5
                else:
                    self.strength = 4
            else:
                if filtered_cards_by_suit.count(2) == 2 and jokers == 1:
                    self.strength = 5
                else:
                    self.strength = 4

        elif (max_val + jokers) == 2:
            if filtered_cards_by_suit.count(2) == 2:
                self.strength = 3
            else:
                self.strength = 2
        else:
            self.strength = 1
    

    def __str__(self):
        print(f'Cards: {self.cards}\tBid: {self.bid}\n\tStrength: {self.strength}')
    

    def __lt__(self, other):
        if isinstance(other, CamelCard):
            if self.strength > other.strength:
                return False
            elif self.strength == other.strength:
                for i in range(len(self.cards)):
                    if self.cards[i] > other.cards[i]:
                        return False
                    elif self.cards[i] == other.cards[i]:
                        continue
                    else:
                        return True
            else:
                return True



if __name__ == '__main__':
    CamelCards()
