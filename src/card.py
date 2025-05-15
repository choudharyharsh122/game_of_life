from dataclasses import dataclass
from typing import Optional
from src.database import get_card_data_by_name

@dataclass
class Card:
    name: str
    intelligence: int
    power: int
    hp: int
    defense: int
    mobility: int
    stealth: int
    g_max: float
    log_base_stealth: float

    @staticmethod
    def from_db(name: str) -> Optional["Card"]:
        data = get_card_data_by_name(name)
        if data:
            _, name, intel, power, hp, defense, mobility, stealth, g_max, log_base = data
            return Card(name, intel, power, hp, defense, mobility, stealth, g_max, log_base)
        return None

    def __str__(self):
        return (f"{self.name} — INT:{self.intelligence}, POW:{self.power}, HP:{self.hp}, "
                f"DEF:{self.defense}, MOB:{self.mobility}, STL:{self.stealth}")