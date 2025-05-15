import random
from typing import List
from src.card import Card
from src.database import get_all_cards

class Player:
    def __init__(self, name: str):
        self.name = name
        self.deck: List[Card] = self._build_deck()
        self.hand: List[Card] = []
        self.draw_hand()

    def _build_deck(self) -> List[Card]:
        all_card_data = get_all_cards()
        deck = []
        for data in all_card_data:
            _, name, intel, power, hp, defense, mobility, stealth, g_max, log_base = data
            for _ in range(random.randint(2, 4)):  # Add 2–4 copies randomly
                deck.append(Card(name, intel, power, hp, defense, mobility, stealth, g_max, log_base))
        random.shuffle(deck)
        return deck

    def draw_hand(self):
        self.hand = []
        for _ in range(5):
            if self.deck:
                self.hand.append(self.deck.pop())

    def show_hand(self):
        print(f"{self.name}'s Hand:")
        for i, card in enumerate(self.hand):
            print(f"{i+1}. {card}")