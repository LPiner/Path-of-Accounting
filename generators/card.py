from typing import Optional

from generators.rarity import generate_rarity
from models.card import Card
from models.prophecy import Prophecy


def generate_card(text: str) -> Optional[Card]:
    text = text.strip()
    type = text.splitlines()[1]
    return Card(
        type=type,
    )



