import random

class Deck:
    def __init__(self):
        self.cards = [{'Two of Hearts': 2}, {'Two of Spades': 2}, {'Two of Clubs': 2}, {'Two of Diamonds': 2},
                      {'Three of Hearts': 3}, {'Three of Spades': 3}, {'Three of Clubs': 3}, {'Three of Diamonds': 3},
                      {'Four of Hearts': 4}, {'Four of Spades': 4}, {'Four of Clubs': 4}, {'Four of Diamonds': 4},
                      {'Five of Hearts': 5}, {'Five of Spades': 5}, {'Five of Clubs': 5}, {'Five of Diamonds': 5},
                      {'Six of Hearts': 6}, {'Six of Spades': 6}, {'Six of Clubs': 6}, {'Six of Diamonds': 6},
                      {'Seven of Hearts': 7}, {'Seven of Spades': 7}, {'Seven of Clubs': 7}, {'Seven of Diamonds': 7},
                      {'Eight of Hearts': 8}, {'Eight of Spades': 8}, {'Eight of Clubs': 8}, {'Eight of Diamonds': 8},
                      {'Nine of Hearts': 9}, {'Nine of Spades': 9}, {'Nine of Clubs': 9}, {'Nine of Diamonds': 9},
                      {'Ten of Hearts': 10}, {'Ten of Spades': 10}, {'Ten of Clubs': 10}, {'Ten of Diamonds': 10},
                      {'Jack of Hearts': 11}, {'Jack of Spades': 11}, {'Jack of Clubs': 11}, {'Jack of Diamonds': 11},
                      {'Queen of Hearts': 12}, {'Queen of Spades': 12}, {'Queen of Clubs': 12}, {'Queen of Diamonds': 12},
                      {'King of Hearts': 13}, {'King of Spades': 13}, {'King of Clubs': 13}, {'King of Diamonds': 13},
                      {'Ace of Hearts': 14}, {'Ace of Spades': 14}, {'Ace of Clubs': 14}, {'Ace of Diamonds': 14},]
        self.player1 = []
        self.player2 = []
    
    def shuffle(self):
        shuffled_deck = random.sample(self.cards, k=len(self.cards))
        return shuffled_deck

    def deal(self):
        deck = self.shuffle()
        p1_hand = []
        p2_hand = []
        for card in range(52):
            if card % 2 == 0:
                p1_hand.append(deck[card])
            else:
                p2_hand.append(deck[card])

        sum1 = 0
        sum2 = 0

        for hand1 in p1_hand:
            for key, value in hand1.items():
                sum1 += int(value)

        for hand2 in p2_hand:
            for key, value in hand2.items():
                sum2 += int(value)

        grand_total = sum1 + sum2

        return p1_hand, p2_hand


def start_menu():
    print(f"""
What would you like to do?
1. Start a new game
2. Exit
          """)
    return input()

if __name__ == '__main__':
    deck = Deck()
    if start_menu() == '1':
        print("They want to start.")
        p1, p2 = deck.deal()
        print(f"These are the cards Player One holds:\n{p1}\n")
        print(f"These are the cards Player Two holds:\n{p2}")
    else:
        print("They want to exit.")

